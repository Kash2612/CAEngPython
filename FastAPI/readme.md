`Once you start implementing, please go ahead with Database integration as well, use sqlite or any database of your choice.`

Use **Models** and **Serializers** for properly handling the data when dealing with databases.


### Admin Endpoints

1. **View All Rides**
    - **Endpoint:** `GET /admin/rides`
    - **Description:** Admins can view all rides in the amusement park with details such as age limit, height limit, and price.
2. **Add a New Ride**
    - **Endpoint:** `POST /rides`
    - **Description:** Admins can add a new ride, including details such as name, age limit, height limit, and price.
3. **Update Ride Information**
    - **Endpoint:** `PUT /rides/<ride_id>`
    - **Description:** Admins can update existing ride details.
4. **Delete a Ride**
    - **Endpoint:** `DELETE /rides/<ride_id>`
    - **Description:** Admins can remove a ride from the park.


### User Endpoints

1. **View All Rides**
    
    - **Endpoint:** `GET /rides`
    - **Description:** Users can view a list of all rides available in the amusement park with details such as age limit, height limit, and price.
2. **Check Eligible Rides and Total Price**
    
    - **Endpoint:** `POST /`
    - **Description:** Users submit their age and height to find rides they are eligible for, along with the total price for those rides.
3. **Login**

    - **Endpoint:** `POST /login`
    - **Description:** Users can log in using their credentials.
4. **Logout**
    
    - **Endpoint:** `GET /logout`
    - **Description:** Users can log out from their session.