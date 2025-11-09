from my_script import db
  

def get_available_mentors():
    try:
        mentors_ref = db.collection("users").where("role", "==", "mentor").stream()

        mentors = []
        for mentor in mentors_ref:
            mentor_data = mentor.to_dict()
            mentors.append({
                "id": mentor.id,
                "name": mentor_data.get("name", "Unknown"),
                "expertise": mentor_data.get("expertise", []),
                "availability": mentor_data.get("availability", [])
            })
        if mentors:
            print(f"found {len(mentors)} mentors(s):")   
            for m in mentors:
                print(f"- {m['name']} ({','.join(m['expertise'])})") 
        else:
            print("No mentors available right now")        

        return mentors  # Return instead of print
    except Exception as e:
        print(f" Error fetching mentors: {e}")   
        return [] 


  
