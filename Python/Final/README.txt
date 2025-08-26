1. Have Docker installed
2. Make Docker Volume
    docker volume create postgres

3. Clone Git Repo in VS Code
4. Install the Container Tools extension
5. In the docker-compose.yml file, click run all services at the top
6. Visit http://localhost:8080/adminer
7. Login
    system: PostgreSQL
    server: postgresql
    username: postgres
    password: postgres
    database: postgres

8. Import the SQL table 
    On the left hand column click Import, then File upload
    Choose Files
    Execute

9. Run the JeopardyMJB.py file and enjoy!