# Task Manager

### Hexlet tests, linter status and Action status:
[![Actions Status](https://github.com/painkiller2001/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/painkiller2001/python-project-52/actions) [![Python CI](https://github.com/painkiller2001/python-project-83/actions/workflows/python-ci.yml/badge.svg)](https://github.com/painkiller2001/python-project-83/actions/workflows/python-ci.yml)
### SonarQube:
[![Quality gate status](https://sonarcloud.io/api/project_badges/measure?project=painkiller2001_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=painkiller2001_python-project-52) [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=painkiller2001_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=painkiller2001_python-project-52) [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=painkiller2001_python-project-52&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=painkiller2001_python-project-52) [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=painkiller2001_python-project-52&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=painkiller2001_python-project-52) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=painkiller2001_python-project-52&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=painkiller2001_python-project-52) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=painkiller2001_python-project-52&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=painkiller2001_python-project-52) [![Maintainability issues](https://sonarcloud.io/api/project_badges/measure?project=painkiller2001_python-project-52&metric=software_quality_maintainability_issues)](https://sonarcloud.io/summary/new_code?id=painkiller2001_python-project-52) [![Reliability issues](https://sonarcloud.io/api/project_badges/measure?project=painkiller2001_python-project-52&metric=software_quality_reliability_issues)](https://sonarcloud.io/summary/new_code?id=painkiller2001_python-project-52) [![Security issues](https://sonarcloud.io/api/project_badges/measure?project=painkiller2001_python-project-52&metric=software_quality_security_issues)](https://sonarcloud.io/summary/new_code?id=painkiller2001_python-project-52) [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=painkiller2001_python-project-52&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=painkiller2001_python-project-52) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=painkiller2001_python-project-52&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=painkiller2001_python-project-52)

Task Manager is a web application designed for organizing and tracking work across a team. It allows users to register and authenticate, create tasks with statuses and labels, assign performers, and filter the task list to monitor progress efficiently.

🌐 Live Demo
The project is successfully deployed on Render and is ready for testing at the link below:

**[Launch Task Manager](https://task-manager-vdvb.onrender.com/)** 🚀

Core Features
User Management: Registration, login/logout, and profile editing — users can only update or delete their own account.
Task Management: Full CRUD for tasks, including name, description, status, assigned performer, and labels.
Statuses & Labels: Create, update, and delete custom statuses and labels to organize tasks the way your team works.
Smart Filtering: Filter the task list by status, performer, label, or show only tasks created by the current user.
Data Integrity Rules: Statuses and labels linked to existing tasks cannot be deleted, and tasks can only be deleted by their original author.
