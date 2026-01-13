from flask import request, jsonify
from src.app.__init__ import db, app
from src.app.model.profile import Profile
from src.app.model.account import Account
from src.app.model.post import Post
from src.app.model.relation import Relation


# Create a profile
@app.route('/profiles', methods=['POST'])
def add_profile():
    data = request.get_json()
    new_profile = Profile(
        account_id=data['account_id'],
        name=data['name'],
        location=data.get('location'),
        lattitude=data.get('lattitude'),
        longitude=data.get('longitude'),
        size=data.get('size'),
        availability=data.get('availability'),
        interests=data.get('interests'),
        metadata=data.get('metadata')
    )
    db.session.add(new_profile)
    db.session.commit()
    return jsonify({"message": "Profile created", "id": new_profile.id}), 201

# Read a profile by ID
@app.route('/profiles/<int:id>', methods=['GET'])
def get_profile(id):
    profile = Profile.query.get_or_404(id)
    return jsonify({
        "id": profile.id,
        "account_id": profile.account_id,
        "name": profile.name,
        "location": profile.location,
        "lattitude": profile.lattitude,
        "longitude": profile.longitude,
        "size": profile.size,
        "availability": profile.availability,
        "interests": profile.interests,
        "metadata": profile.metadata
    }), 200

# Edit a profile
@app.route('/profiles/<int:id>', methods=['PUT'])
def edit_profile(id):
    profile = Profile.query.get_or_404(id)
    data = request.get_json()

    profile.name = data.get('name', profile.name)
    profile.location = data.get('location', profile.location)
    profile.lattitude = data.get('lattitude', profile.lattitude)
    profile.longitude = data.get('longitude', profile.longitude)
    profile.size = data.get('size', profile.size)
    profile.availability = data.get('availability', profile.availability)
    profile.interests = data.get('interests', profile.interests)
    profile.metadata = data.get('metadata', profile.metadata)

    db.session.commit()
    return jsonify({"message": "Profile updated"}), 200

# Delete a profile
@app.route('/profiles/<int:id>', methods=['DELETE'])
def delete_profile(id):
    profile = Profile.query.get_or_404(id)
    db.session.delete(profile)
    db.session.commit()
    return jsonify({"message": "Profile deleted"}), 200
