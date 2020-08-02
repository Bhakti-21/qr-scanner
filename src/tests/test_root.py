import json


def test_index(app, client):
	res = client.get('/')
	print("res", res, res.status_code)
	assert res.status_code == 200
	expected = {'hello': 'world'}
	assert expected == json.loads(res.get_data(as_text=True))



def test_user_details(app, client):
	res = client.get('/9892291701?username=bhakti&password=bhakti@123')
	assert res.status_code == 200
	assert 'phone_no' in json.loads(res.get_data(as_text=True))
	assert 'reason' not in json.loads(res.get_data(as_text=True))




def test_post_details(app, client):
	mimetype = 'application/json'
	headers = {
		'Content-Type': mimetype,
		'Accept': mimetype
		}
	post_data = {	
		"phone_no":"7738412825",
		"username":"prakash",
		"dob":"14-02-1956",
		"age":"64",
		"gender":"Female",
		"aadhar_no":"789456",
		"image_url" : "https://res.cloudinary.com/demo/image/upload/w_500/sample.jpg"
	}

	post_data = json.dumps(post_data)
	res = client.post('/userdetails?username=prakash&password=prakash@123', data=post_data, headers=headers)
	assert res.json == 'successful'
	assert res.status_code == 200



def test_post_details(app, client):
	mimetype = 'application/json'
	headers = {
		'Content-Type': mimetype,
		'Accept': mimetype
		}
	post_data = {	
		"phone_no":"7738412825",
		"username":"prakash",
		"dob":"14-02-1956",
		"age":"64",
		"aadhar_no":"789456",
		"image_url" : "https://res.cloudinary.com/demo/image/upload/w_500/sample.jpg"
	}

	post_data = json.dumps(post_data)
	res = client.post('/userdetails?username=prakash&password=prakash@123', data=post_data, headers=headers)
	assert res.json == 'successful'
	assert res.status_code == 200
