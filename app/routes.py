
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from app.models import db, Skill, Project, Certification

main = Blueprint('main', __name__)

@main.route('/')
def index():
    technical_skills = Skill.query.filter_by(category="technical").all()
    soft_skills = Skill.query.filter_by(category="soft").all()
    tools_skills = Skill.query.filter_by(category="tools").all()
    projects = Project.query.all()
    certifications = Certification.query.all()
    
    return render_template('index.html', 
                        technical_skills=technical_skills,
                        soft_skills=soft_skills,
                        tools_skills=tools_skills,
                        projects=projects,
                        certifications=certifications)

@main.route('/admin/skill', methods=['POST'])
def add_skill():
    data = request.json
    skill = Skill(
        name=data['name'],
        icon=data['icon'],
        category=data['category'],
        proficiency=data.get('proficiency', 0)
    )
    db.session.add(skill)
    db.session.commit()
    return jsonify(skill.to_dict()), 201

@main.route('/admin/skill/<int:skill_id>', methods=['DELETE'])
def delete_skill(skill_id):
    skill = Skill.query.get_or_404(skill_id)
    db.session.delete(skill)
    db.session.commit()
    return '', 204

@main.route('/admin/project', methods=['POST'])
def add_project():
    data = request.json
    project = Project(
        title=data['title'],
        description=data['description'],
        icon=data['icon'],
        category=data['category'],
        live_link=data.get('live_link'),
        code_link=data.get('code_link'),
        tags=','.join(data.get('tags', []))
    )
    db.session.add(project)
    db.session.commit()
    return jsonify(project.to_dict()), 201

@main.route('/admin/project/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return '', 204

@main.route('/admin/certification', methods=['POST'])
def add_certification():
    data = request.json
    cert = Certification(
        title=data['title'],
        provider=data['provider'],
        year=data['year'],
        icon=data['icon'],
        link=data.get('link')
    )
    db.session.add(cert)
    db.session.commit()
    return jsonify(cert.to_dict()), 201

@main.route('/admin/certification/<int:cert_id>', methods=['DELETE'])
def delete_certification(cert_id):
    cert = Certification.query.get_or_404(cert_id)
    db.session.delete(cert)
    db.session.commit()
    return '', 204
