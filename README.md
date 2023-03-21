# Introdução
Esta documentação tem como objetivo explicar o projeto da lambda function, que é uma aplicação desenvolvida para ser executada em um ambiente cloud, preferencialmente em lambdas na AWS. A aplicação recebe dois parâmetros via requisição HTTP: bucket_name e object_key, que referem-se a um arquivo CSV em um bucket do s3. A função lê o arquivo no bucket, trata as informações e salva em um banco de dados de preferência do desenvolvedor.
## Pré-requisitos
Conta na AWS com permissões para criar lambdas, S3 e acesso a um banco de dados.
## Instruções para instalação e execução
1. Faça o clone do repositório da aplicação.

2. Certifique-se de ter instalado na sua máquina a AWS CLI e o boto3, biblioteca python para interagir com os serviços da AWS.

3. No console AWS, crie um bucket no S3 e adicione um arquivo CSV para teste.

4. Crie uma tabela no banco de dados escolhido para armazenar as informações do CSV.

5. Abra o arquivo lambda_function.py e substitua as informações referentes ao seu banco de dados, como usuário, senha, nome da tabela, nome das colunas e tipos de dados.

6. Crie uma nova função lambda na AWS, escolha a opção "Criar função do zero" e defina um nome e uma descrição para a função.

7. Na configuração da função lambda, escolha o tempo de execução, que deve ser o mesmo utilizado no arquivo lambda_function.py. Também será necessário criar uma role que permita que a função tenha acesso aos serviços utilizados.

8. No editor de código da função, cole o conteúdo do arquivo lambda_function.py.

9. Clique em "Teste" e preencha os parâmetros bucket_name e object_key com o nome do bucket e o caminho do arquivo no S3.

10. Clique em "Testar" e aguarde o resultado.
