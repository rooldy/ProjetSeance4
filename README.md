# ProjetSeance4
Data streaming Projet : Ce projet a pour objectif de mettre en place un processus de transmission d'un flux continu de données, également connu sous le nom de flux ou data streaming, qui est introduit dans un logiciel de traitement de flux afin d'en tirer des informations précieuses en temps réel.

# Etape d'installation
Cette section consiste à expliquer comment installer et configurer le projet.
Pour réaliser ce projet j'ai fait le choix d'utiliser un environnement virtuel qui en quelque sorte une pratique très importante pour garantir que votre projet fonctionne correctement avec ses dépendances spécifiques, éviter les conflits avec d'autres projets, faciliter la configuration et faciliter la collaboration avec d'autres développeurs.

<br/>Pour créer cet environnement virtuel :
  <br/> 1-Lancer la commande pip install virtualenv setuptools wheel
   <br/> 2-Lancer la commande pip install --upgrade pip ou python -m pip install --upgrade pip
   <br/> 3-Créer un environnement virtuel avec la commande : python -m venv venv
  <br/>  4-Activer l'environnement virtuel avec la commande :
         <br/>windows : .\venv\Scripts\activate
        <br/> mac ou linux :source ./venv/bin/activate
        
 Dans un fichier requirements.txt j'ai ajouté toutes les librairies que j'aurai besoin pour réaliser ce projet et pour les installer il suffira de lancer la commande  :
     
     pip install -r requirements.txt pour les installer.
     
# Configuration de docker

Il a été demandé de créer une instance de rabbitmq qui est souvent utilisé dans les architectures de microservices pour gérer la communication entre les différents services. Il peut également être utilisé pour les applications de traitement en arrière-plan, les systèmes de messagerie instantanée et les systèmes de notification.
On a crée un fichier .env qui contient toutes les informations de connexions et par la suite on a exécuté la commande:

    docker-compose --env-file .env -f docker-compose.yml -p data-stream up -d
 
   
