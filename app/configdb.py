    # import mysql.connector 

    # #from config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

    # def conectar():
    #     conexao = mysql.connector.connect(
    #         host=mysql,
    #         port=3306,
    #         user=root,
    #         password=aluno,
    #         database='dashboard_formativa'
    #     )
    #     return conexao
    
import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="localhost",    
        port=3306,
        user="root",         
        password="aluno",    
        database="dashboard_formativa"
    )
    return conexao