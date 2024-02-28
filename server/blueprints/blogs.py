from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt, current_user
from models import Blog, db
from schemas import BlogSchema

blog_bp = Blueprint('blogs', __name__)

@blog_bp.route('/new', methods=['POST'])
@jwt_required()
def create_blog():
    # Check user's role
    if current_user.role not in ['superadmin', 'admin']:
        return jsonify({"message": "Unauthorized access"}), 401
    
    data = request.get_json()
    new_blog = Blog(
        title= data.get('title'),
        description=data.get('description'),
        blog_img = "images/blogs/blog1.png"
    )

    new_blog.save()

    return jsonify({"message": "Blog created successfully"}), 201

@blog_bp.route('/<int:blog_id>', methods=['GET'])
def get_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    response = BlogSchema().dump(blog)
    return jsonify(response), 200

@blog_bp.route('/all', methods=['GET'])
def get_all_blogs():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', type=int)

    blogs = Blog.query.paginate(
        page = page,
        per_page = per_page
    )
        
    response = BlogSchema().dump(blogs, many=True)

    return jsonify(response), 200

@blog_bp.route('/update/<int:blog_id>', methods=['PUT'])
@jwt_required()
def update_blog(department_id):
    # Check user's role
    if current_user.role not in ['superadmin', 'admin']:
        return jsonify({"message": "Unauthorized access"}), 401
    
    blog = Blog.query.get_or_404(department_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(blog, key, value)
    db.session.commit()
    return jsonify({"message": "Blog updated successfully"}), 200

@blog_bp.route('/delete/<int:blog_id>', methods=['DELETE'])
@jwt_required()
def delete_blog(blog_id):
    # Check user's role
    if current_user.role not in ['superadmin', 'admin']:
        return jsonify({"message": "Unauthorized access"}), 401
    
    blog = Blog.query.get_or_404(blog_id)
    db.session.delete(blog)
    db.session.commit()
    return jsonify({"message": "Blog deleted successfully"}), 200