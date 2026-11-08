def test_create_and_read(client,auth_headers,sample_payload):
 r=client.post("/api/non-conformities",json=sample_payload,headers=auth_headers);assert r.status_code==201
 data=r.json();assert data["title"]==sample_payload["title"] and data["code"].startswith("NC-")
 read=client.get(f"/api/non-conformities/{data['id']}",headers=auth_headers);assert read.status_code==200 and read.json()["id"]==data["id"]
def test_update_and_delete_persist(client,auth_headers,sample_payload):
 item=client.post("/api/non-conformities",json=sample_payload,headers=auth_headers).json()
 upd=client.put(f"/api/non-conformities/{item['id']}",json={"status":"Em tratamento"},headers=auth_headers);assert upd.status_code==200 and upd.json()["status"]=="Em tratamento"
 assert client.delete(f"/api/non-conformities/{item['id']}",headers=auth_headers).status_code==200
 assert client.get(f"/api/non-conformities/{item['id']}",headers=auth_headers).status_code==404
