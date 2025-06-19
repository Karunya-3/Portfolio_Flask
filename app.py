from flask import Flask, render_template

app = Flask(__name__)

# Dummy project data
projects = [
    {
        'id': 1,
        'title': 'IV&V Automation Tool',
        'description': 'A tool that compares templates with project documents to generate observation reports.',
        'technologies': ['React', 'Javascript', 'HTML5', 'CSS3','Bootstrap'],
        'image': 'images/nstl.png',
        'details': 'Developed a web-based IV&V (Independent Verification and Validation) automation tool to streamline the process of comparing project documents with predefined templates. Implemented features for file upload, content extraction, template matching, and automated observation report generation. Used React for the frontend and integrated backend logic to process and analyze document data. Focused on enhancing usability, reducing manual effort, and ensuring consistency in validation reporting.',
        'github_link': 'https://github.com/Karunya-3/Automation',
        'live_demo': 'https://automation-umber.vercel.app/'
    },
    {
        'id': 2,
        'title': 'Role Radar',
        'description': 'A tool to identify industry veterans based on minimal inputs like domain and keywords.',
        'technologies': ['Flask', 'NLP techniques', 'API Integration', 'HTML5', 'CSS3'],
        'image': 'images/roleradar.png',
        'details': 'Built a smart tool to identify industry veterans with 10+ years of experience based on minimal inputs like domain and keywords. Designed an intuitive interface to input search criteria and integrated logic to filter expert profiles from large datasets. The system aims to assist organizations in quickly locating qualified domain experts for hiring, consulting, or mentorship roles. Focused on usability, accuracy, and speed to ensure reliable expert discovery.',
        'github_link': 'https://github.com/Karunya-3/RoleRadar',
        'live_demo': 'https://roleradar-01.onrender.com/'
    },
]

skills = {
    'Frontend': ['HTML5, CSS3', 'JavaScript', 'React', 'Bootstrap','Flask'],
    'Languages': ['Python', 'C', 'C++', 'Java'],
    'Libraries': ['NumPy', 'Pandas', 'Scikit-learn', 'Flask'],
    'Tools': ['Git', 'Canva'],
    'Database': ['MySQL'],
    'Soft Skills': ['Problem Solving', 'Teamwork', 'Communication', 'Adaptability']
    
}

@app.route('/')
def index():
    return render_template('index.html', projects=projects, skills=skills)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in projects if p['id'] == project_id), None)
    if project is None:
        return "Project not found", 404
    return render_template('project_detail.html', project=project)

if __name__ == '__main__':
    app.run(debug=True)