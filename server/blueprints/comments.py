from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, current_user
from models import Comment, db, Blog
from schemas import CommentSchema

comment_bp = Blueprint('comments', __name__)

@comment_bp.route('/blog/<int:blog_id>', methods=['GET'])
def get_comments_for_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    comments = Comment.query.filter_by(blog_id=blog_id).all()
    response = CommentSchema(many=True).dump(comments)
    return jsonify(response), 200

@comment_bp.route('/blog/<int:blog_id>/new', methods=['POST'])
@jwt_required()
def create_comment_for_blog(blog_id):
    data = request.get_json()
    blog = Blog.query.get_or_404(blog_id)
    new_comment = Comment(
        comment=data.get('comment'),
        user_id=current_user.id,
        blog_id=blog_id
    )
    new_comment.save()
    return jsonify({"message": "Comment created successfully"}), 201

@comment_bp.route('/blog/<int:blog_id>/<int:comment_id>', methods=['GET'])
def get_comment_for_blog(blog_id, comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if comment.blog_id != blog_id:
        return jsonify({"message": "Comment does not belong to this blog"}), 404
    response = CommentSchema().dump(comment)
    return jsonify(response), 200

@comment_bp.route('/blog/<int:blog_id>/<int:comment_id>', methods=['PUT'])
@jwt_required()
def update_comment_for_blog(blog_id, comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if comment.user_id != current_user.id:
        return jsonify({"message": "Unauthorized"}), 403
    if comment.blog_id != blog_id:
        return jsonify({"message": "Comment does not belong to this blog"}), 404
    data = request.get_json()
    comment.comment = data.get('comment')
    db.session.commit()
    return jsonify({"message": "Comment updated successfully"}), 200

@comment_bp.route('/blog/<int:blog_id>/<int:comment_id>', methods=['DELETE'])
@jwt_required()
def delete_comment_for_blog(blog_id, comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if comment.user_id != current_user.id:
        return jsonify({"message": "Unauthorized"}), 403
    if comment.blog_id != blog_id:
        return jsonify({"message": "Comment does not belong to this blog"}), 404
    db.session.delete(comment)
    db.session.commit()
    return jsonify({"message": "Comment deleted successfully"}), 200
