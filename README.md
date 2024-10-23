# Projeto de Reconhecimento Facial para Controle de Entrada

Este projeto utiliza reconhecimento facial para controlar a entrada em um prédio residencial. Ele detecta rostos em tempo real e compara com um banco de dados de pessoas autorizadas. Quando o rosto reconhecido corresponde a uma pessoa autorizada, o sistema libera o acesso.

#Funcionalidades

-Captura de vídeo em tempo real usando a webcam.

-Detecção de rostos na imagem capturada.

-Comparação de rostos capturados com um banco de dados de imagens autorizadas.

-Exibição de uma mensagem indicando se o acesso é liberado ou negado.


#Requisitos

Antes de começar, é necessário instalar algumas bibliotecas Python e garantir que a estrutura de pastas esteja corretamente configurada.

-Bibliotecas Python

Instale as bibliotecas necessárias usando o comando abaixo:

-pip install opencv-python face_recognition

OpenCV: Usado para capturar vídeo da webcam e exibir a imagem.

face_recognition: Usado para detecção e reconhecimento facial. É uma biblioteca construída sobre o dlib.


# Estrutura de Pastas

Organize o projeto da seguinte forma:

/facial-recognition-project
│
├── /authorized_images         # Pasta para armazenar as imagens das pessoas autorizadas
│   └── pessoa_autorizada.jpg  # Exemplo de imagem de uma pessoa autorizada
│
├── facial_recognition.py     # Script principal do reconhecimento facial
└── README.md                 # Documentação do projeto

Certifique-se de que a imagem da pessoa autorizada esteja dentro da pasta authorized_images e siga o nome de arquivo correto no código.

# Como Executar o Projeto

1. Clonar ou baixar o projeto:

git clone https://github.com/seu-usuario/facial-recognition-project.git
cd facial-recognition-project


2. Adicionar imagens de pessoas autorizadas:

Adicione imagens das pessoas autorizadas à pasta authorized_images. No código, altere o caminho das imagens se necessário.

Exemplo de alteração no código:

authorized_image = face_recognition.load_image_file("authorized_images/pessoa_autorizada.jpg")


3. Executar o script:

Execute o script principal para iniciar o reconhecimento facial:

python facial_recognition.py


4. Encerrar o programa:

Pressione q para encerrar a execução e liberar a câmera.



# Melhorias Futuras

Adicionar suporte para múltiplos rostos autorizados.

Integrar com sistemas de controle de portas.

Implementar notificação de tentativa de acesso negada.

Melhorar a precisão com ângulos variados do rosto.


# Problemas Conhecidos

Em condições de baixa iluminação, a detecção de rosto pode ser menos eficiente.

Dependendo da qualidade da câmera, o reconhecimento pode apresentar variações.


Contribuições

Se você deseja contribuir para o projeto, sinta-se à vontade para fazer um fork e enviar suas modificações via pull request.


---

Com essa documentação, você tem o caminho necessário para rodar o projeto eficientemente. Certifique-se de ajustar o nome da imagem na pasta authorized_images e testar com uma boa iluminação e uma webcam de qualidade razoável.

