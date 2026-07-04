# Análise de Porto/Embarcação

Esse projeto tem como objetivo automatizar o processo de análise da alocação das embarcações em seus respectivos portos.

Para cada registro contábil é atribuído um código de porto e um código de embarcação. No final de cada período é enviado pelo setor responsável
a informação da localização de cada embarcação. Utilizando uma planilha excel, seguimos os passos: 

1. Criamos uma aba "Alocação" onde é preenchido com as informações sobre a localização das embarcações no final do período e identificamos com
   os códigos dos respectivos portos e embarcações.

   <img width="473" height="219" alt="image" src="https://github.com/user-attachments/assets/5b4b53ef-816f-4480-b1ec-1178b243fab1" />

2. Criamos uma aba "Base" que recebe os registros contábeis que serão analisados.

   <img width="416" height="449" alt="image" src="https://github.com/user-attachments/assets/6f16a529-9140-4247-ad4e-154a96981b8c" />

3. Na aplicação, selecionamos o arquivo contendo as informações anteriores para análise.

   <img width="597" height="329" alt="image" src="https://github.com/user-attachments/assets/853b363b-37a6-4da1-bf9d-0958d613a8ed" />

4. Selecionamos o destino do arquivo processado com as inconsistências.

   <img width="604" height="229" alt="image" src="https://github.com/user-attachments/assets/a078f84a-f1f1-41ab-b816-dbcf4b961e8e" />

5. Executamos o processamento do arquivo.

  <img width="587" height="138" alt="image" src="https://github.com/user-attachments/assets/a8e21f27-e180-4699-9680-1f41fc70625d" />

6. O sistema gerará um arquivo excel com as inconsistências separadas por abas, onde as abas estarão identificadas com o código do porto onde essas
   embarcações deveriam estar alocadas.

  <img width="458" height="218" alt="image" src="https://github.com/user-attachments/assets/0ff3c670-ecdb-40e0-ad14-f14ad983df2b" />

