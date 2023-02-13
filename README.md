# Poké battle API

Poké battle API is a backend API application for the point and click game PokéBattle!

## Contents

- [Goals](#goals)
- [User Stories](#user-stories)
    - [Profiles](#profiles)
    - [Pokémon](#pokémon)
    - [Items](#items)
    - [Movesets](#movesets)
    - [Battles](#battles)
- [API Endpoints](#api-endpoints)
- [Database Design](#database-design)
- [Security](#security)
- [Technologies Used](#technologies-used)
- [Python Packages](#python-packages)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

---

## Goals

The goal of this API is to allow the front end application of PokéBattle to perform Create, Read, Update and Delete functionality via User Interaction.

---

## User Stories

The user stories below are in order of planned implementation.

### Profiles

- As a **user** I can **create a profile** so that **I can capture and train Pokémon**
- As a **user** I can **update my profile** so that **I can add a profile image and change my username**
- As a **developer** I can **access a users battle milestones** so that **I can update their Pokémart to have better items; trainer battles to be more challenging, and to know which boss/ gym leader will be next in line for the next boss/ gym battle**

---

### Pokémon

*Everything here is related to all screens where you can view and/or change Pokémon information*

- As a **user** I can **see my owned Pokémon** so that **I can change my lineup if required**
- As a **user** I can **access a Pokédex** so that **I can see all Pokémon I have encountered and caught and their base stats**
- As a **developer** I can **access the details of a Pokémon** so that **I can show the user Pokémon stats and moves, and use these in battles**
- As a **user** I can **update the nickname of my Pokémon** so that **I can know which Pokémon is which without looking at stats and so that I can make the Pokémon feel more unique**
- As a **user** I can **view my current Pokémon party** so that **I can see who will be in my next battle**
- As a **user** I can **organise my party** so that **I can decide which Pokémon will be first in a battle**
- As a **developer** I can **have access to each evolution of each Pokémon** so that **I can evolve a Pokémon at the appropriate time if the user would like that Pokémon to evolve**
- As a **developer** I can **remove an evolved Pokémon** so that **the users Pokémon count doesn't increase when their Pokémon is supposed to evolve**
- As a **user** I can **remove a Pokémon from my owned Pokémon** so that **I can clear out some space for other Pokémon and make the space look neater**

---

### Items

*Everything here is related to anything that may involve viewing items*

- As a **user** I can **access a Pokémart** so that **I can purchase items to prepare for battles**
- As a **user** I can **see the items I own** so that **I can use them to improve my Pokémon stats, or know what I need to purchase from the Pokémart**
- As a **developer** I can **access each item individually** so that **I can have an item perform its role appropriately, and let the user purchase the item at the time appropriate to their battle stage**
- As a **developer** I can **remove a used item** so that **a user can't use the item again without purchase if they don't have more**
- As a **user** I can **remove an item I don't want anymore** so that **I can clear out space for items that I need**

---

### MoveSets

- As a **developer** I can **all TM (technical machine) info** so that **I can make sure only the appropriate Pokémon for that TM can learn the move and display it to the user as appropriate**
- As a **developer** I can **access a Pokémons moveset** so that **I can determine which calculation needs to be made when each move is used**

---

### Battles

- As a **user** I can **view all my previous battles** so that **I can see the progress I've made with each Pokémon**
- As a **developer** I can **access all information of an in progress battle** so that **I know which moves and Pokémon are available, and adjust the battle as required by what's been done by the user and computer**
- As a **user** I can **see the current HP of both Pokémon in battle** so that **I can make strategic choices on what to do next in battle**

---

## API Endpoints

### Profiles

GET/PUT `../profiles/<id>`

- id = resource identifier (integer)
- owner = user connection (one to one field connected to django User)
- created_at = profile creation date (date time field)
- name = optional name of user (Char field max 250 characters)
- content = optional description of user (Text field)
- profile_image = optional image for user (Image field)
- balance = money held by user (integer)
- gym_category = the next gym to be defeated (integer)
- tutorial_level = how much tutorial is completed (integer)
- trainer_type = the type of trainer the user is (Text field, defaults as "Trainer")

*To be completed*

--- 

## Database Design

*To be completed*

---

## Security

*To be completed*

---

## Technologies used

- Django
    - Main framework used for the application
- Django REST Framework
    - Framework used for creating an API (not yet installed)
- Cloudinary
    - Used for hosting static images
- Heroku 
    - Hosts the application
- Git
    - Used for version control
- GitHub 
    - Repository for storing code base and docs

--- 

## Python Packages

*To be completed*

---

## Testing

### Profiles

- I have tested the GET method by opening the link to `../profiles/`, making sure it returns a JSON response for each profile
- I have tested the GET method for Profile details by testing the links to valid and invalid profile id's. I've also made sure the response returned remains in JSON format
- I have tested the PUT method by updating the name and content for a user, making sure the JSON response relevant to what I've updated, changes too

*To be completed*

---

## Deployment

*To be completed*

---

## Credits

*To be completed*

---