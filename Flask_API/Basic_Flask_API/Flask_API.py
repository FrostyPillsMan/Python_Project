from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

class MusicModel(db.Model):
    music_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Music(name = {self.name}, views = {self.views}, likes = {self.likes})"

"""
names = {
            "Adam": {"age": 21, "gender": "Male"},
            "Nhi": {"age": 25, "gender": "Female"}
        }
"""

"""
Scenario 1
class LearnFlask(Resource):
    def get(self, name):
        return names[name]
    
    def post(self, name, age):
        return {"message": f"Hello {name}, you are {age} years old!"}
"""

# api.add_resource(LearnFlask, "/Hi flask!!@@/<string:name>")

music_put_args = reqparse.RequestParser()
music_put_args.add_argument("name", type=str, help="Name of the music", required=True)
music_put_args.add_argument("views", type=int, help="Views of the music", required=True)
music_put_args.add_argument("likes", type=int, help="Likes of the music", required=True)

music_update_args = reqparse.RequestParser()
music_update_args.add_argument("name", type=str, help="Name of the music")
music_update_args.add_argument("views", type=int, help="Views of the music")
music_update_args.add_argument("likes", type=int, help="Likes of the music")

music_disk = {}

resource_fields = {
    'music_id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

"""
Alternatives

def abort_if_music_playlist_not_exist(music_playlist):
    if music_playlist not in music_disk:
        abort(404, description="Music is not valid...")
"""

"""
def abort_if_music_exists(music_playlist):
    if music_playlist in music_disk:
        abort(409, description="Music has existed with that playlist...")
"""

class Music(Resource):
    @marshal_with(resource_fields)
    def get(self, music_playlist):
        result = MusicModel.query.filter_by(music_id=music_playlist).first()
        return result

    """
    def get(self, music_playlist):
        abort_if_music_playlist_not_exist(music_playlist)
        return music_disk[music_playlist]
    """

    """
    def put(self, music_playlist):
        abort_if_music_exists(music_playlist)
        args = music_put_args.parse_args()
        music_disk[music_playlist] = args
        return {
            "message": f"Music '{args['name']}' added successfully!",
            "data": music_disk[music_playlist]
        }, 201
    """

    @marshal_with(resource_fields)
    def put(self, music_playlist):
        args = music_put_args.parse_args()
        result = MusicModel.query.filter_by(music_id=music_playlist).first()
        if result:
            abort(409, description="Music Playlist Taken...")
        music_entry = MusicModel(
            music_id=music_playlist,  # type: ignore
            name=args['name'], # type: ignore
            views=args['views'], # type: ignore
            likes=args['likes'] # type: ignore
        ) # type: ignore
        db.session.add(music_entry)
        db.session.commit()
        return music_entry, 201
    
    @marshal_with(resource_fields)
    def patch(self, music_playlist):
        args = music_update_args.parse_args()
        result = MusicModel.query.filter_by(music_id=music_playlist).first()
        if not result:
            abort(404, description="Music Playlist does not exist, cannot update")
        
        if args['name']:
            result.name = args['name'] # type: ignore
        if  args['views']:
            result.views = args['views'] # type: ignore
        if args['likes']:
            result.likes = args['likes'] # type: ignore
        
        db.session.commit()
        return result

    def delete(self, music_playlist):
        # abort_if_music_playlist_not_exist(music_playlist)
        del music_disk[music_playlist]
        return "The video has been successfully deleted", 204

api.add_resource(Music, "/music/<int:music_playlist>")

if __name__ == "__main__":
    app.run(debug=True, port=5000)

