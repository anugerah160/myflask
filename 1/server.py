from flask import Flask, make_response, request
app = Flask(__name__)

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]

@app.route("/")
def index():
    return "Hello World"

@app.route("/no_content")
def no_content():
    """Return 'No content found' with a status of 204

    Returns:
        string: No content found
        status code: 204

    """
    return ({"message": "No content found"}, 204)

@app.route("/exp")
def index_explicit():
    """return 'Hello World' message with a status code of 200
    Returns:
        string: Hello World
        status code: 200
    """
    resp = make_response({"message" : "Hello World"})
    resp.status_code = 200
    return resp

@app.route("/data")
def get_data():
    try:
        if data and len(data) > 0:
            return {"message" : f"Data of length {len(data)} found"}
        else:
            return {"message" : "Data is empty"}, 500
    except NameError:
        return {"message" : "Data not found"}, 404

@app.route("/name_search")
def name_search():
    """Find a person in the database.

    Returns:
        json: Person if found, with status of 200
        404: If not found 
        422: If argumen 'q' is missing
    """

    #Get the argument 'q' from thequery parameters of the request
    query = request.args.get('q')

    if not query:
        return {"message": "Query parameter 'q' is missing"}, 422

    for person in data:
        if query.lower() in person["first_name"].lower():
            return person
        
    return {"message": "Person not found"}, 404

@app.route("/count")
def count():
    try:
        return {"data count": len(data)}, 200
    except NameError:
        return {"message": "data not defined"}, 500

@app.route("/person/<uuid:id>")
def find_by_uuid(id):
    for person in data:
        if person["id"] == str(id):
            return person
    return {"message": "Person not found"}, 404

@app.route("/person/<uuid:id>", methods=['DELETE'])
def delete_by_uuid(id):
    for person in data:
        if person["id"] == str(id):
            data.remove(person)
            return {"message": f"Person with ID {id} deleted"}, 200
    return {"message": "Person not found"}, 404

@app.route("/person", methods=['POST'])
def add_by_uuid():
    new_person = request.get_json()

    if not new_person:
        return {"message": "Invalid input, no data provided"}, 400

    return {"message": "Person created successfully"}, 200

@app.errorhandler(404)
def api_not_found(error):
    return {"message": "API not found"}, 404
