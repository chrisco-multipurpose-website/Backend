from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt
from models import Comment, db
from schemas import CommentSchema

comment_bp = Blueprint('comments', __name__)

@comment_bp.route('/new', methods=['POST'])
def create_comment():
    data = request.get_json()
    new_comment = Comment(
        content = data.get('content'),
        timestamp = data.get('timestamp')
    )

    new_comment.save()

    return jsonify({"message": "Comment created successfully"}), 201

@comment_bp.route('/<int:comment_id>', methods=['GET'])
def get_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    response = CommentSchema().dump(comment)
    return jsonify(response), 200

@comment_bp.route('/all', methods=['GET'])
def get_all_comments():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', type=int)

    comments = Comment.query.paginate(
        page = page,
        per_page = per_page
    )
        
    response = CommentSchema().dump(comments, many=True)

    return jsonify(response), 200

@comment_bp.route('/update/<int:comment_id>', methods=['PUT'])
# @jwt_required()
def update_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(comment, key, value)
    db.session.commit()
    return jsonify({"message": "Comment updated successfully"}), 200

@comment_bp.route('/delete/<int:comment_id>', methods=['DELETE'])
# @jwt_required()
def delete_depcomment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return jsonify({"message": "Comment deleted successfully"}), 200