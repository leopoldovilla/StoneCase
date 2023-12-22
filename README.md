# StoneCase

- Devido a vários problemas com o ambiente de download da B3, será necessário baixar o arquivo csv manualmente e colocar na pasta data.
- Executar a instalação das dependências do requiments.txt
- Executar a classe main.py para iniciar o projeto

Após iniciado o projeto, os seguintes endpoints estarão disponíveis:

// Atualiza o banco com os dados do arquivo csv
http://127.0.0.1:5000/updateData

// Retorna todos os dados do banco
http://127.0.0.1:5000/data
// Retorna os dados filtrados por ticker
http://127.0.0.1:5000/data?ticker=TF583R
// Retorna os dados filtrados por business_date
http://127.0.0.1:5000/data?business_date=2023-12-12
// Retorna os dados filtrados por ticker e business_date
http://127.0.0.1:5000/data?ticker=TF583R&data=2023-12-12
