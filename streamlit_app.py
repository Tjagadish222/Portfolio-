
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from app.models import Skill, Project, Certification
import os
from config import Config

# Create database engine
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
db_session = scoped_session(sessionmaker(bind=engine))

def main():
    st.title("Professional Portfolio")
    
    # Skills Section
    st.header("Skills")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Technical Skills")
        technical_skills = db_session.query(Skill).filter_by(category="technical").all()
        for skill in technical_skills:
            st.write(f"{skill.name} ({skill.proficiency}%)")
    
    with col2:
        st.subheader("Soft Skills")
        soft_skills = db_session.query(Skill).filter_by(category="soft").all()
        for skill in soft_skills:
            st.write(f"{skill.name} ({skill.proficiency}%)")
    
    with col3:
        st.subheader("Tools")
        tools_skills = db_session.query(Skill).filter_by(category="tools").all()
        for skill in tools_skills:
            st.write(f"{skill.name} ({skill.proficiency}%)")
    
    # Projects Section
    st.header("Projects")
    projects = db_session.query(Project).all()
    for project in projects:
        with st.expander(project.title):
            st.write(project.description)
            if project.live_link:
                st.write(f"[Live Demo]({project.live_link})")
            if project.code_link:
                st.write(f"[Code]({project.code_link})")
            st.write(f"Tags: {project.tags}")
    
    # Certifications Section
    st.header("Certifications")
    certifications = db_session.query(Certification).all()
    for cert in certifications:
        st.write(f"**{cert.title}** - {cert.provider} ({cert.year})")
        if cert.link:
            st.write(f"[View Certificate]({cert.link})")

if __name__ == "__main__":
    main()
