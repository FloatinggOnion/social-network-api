# Social Network API Using Django REST Framework

## About
- This is the backend for a social network written with the Django REST Framework.
- It has a PostgreSQL database.

## User Model
- public_id: string
- first_name: string
- last_name: string
- username: string
- bio: string
- avatar: image
- email: string
- is_active
- is_superuser
- created: datetime
- updated: datetime

## Endpoints
- Get current user: `/api/user`
- Register a new user: `api/auth/register`
- Login a user: `api/auth/login`
- Refresh JWT token: `api/auth.refresh`
- View a post: `api/post`
- Like a post: `api/post/post_pk/like`
- Unlike a post: `api/post/post_pk/unlike`

## Setup

## Task List
- [x] Connect PostgreSQL database
- [x] Abstract models, serializers and viewsets
- [x] Custom User model
- [x] Serialize user models
- [x] Create User Viewsets and Routers
- [x] Setup jwt auth
- [x] Setup authentication (registration, login, logout)
- [x] Create post model
  - [x] Like, remove like, and has liked methods
  - [x] Like count
  - [x] Add like and dislike
- [ ] Add comments to posts
  - [ ] Write comment model
  - [ ] Write comment serializer
  - [ ] Nest routes for comment resource
  - [ ] Update comment
  - [ ] Delete comment
- [ ] Testing
  - [ ] Models
    - [ ] User model
    - [ ] Post model
    - [ ] Comment model
  - [ ] Views
    - [ ] Authentication
    - [ ] Post viewset
    - [ ] Comment viewset
    - [ ] User viewset