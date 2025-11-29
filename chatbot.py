import google.generativeai as genai
key ='ENTER_API_KEY'
genai.configure(api_key=key)
model=genai.GenerativeModel("gemini-2.5-flash")
while True:
  user=input("enter what you want to search or type exit to close : ")
  if user.lower()=="exit":
    print("bye bye")
    break
  response= model.generate_content(user)
  print("bot:",response.text)