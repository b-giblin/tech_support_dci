# Brian Giblin
# 10/25/23
# Tech Support Assignment


def automated_technical_support():
  """
  Function  to simualte an automated technical support system.
  Users input queries and receive a response based on keyword matches.
  """


  # Dictionary containing the keyword-to-response mappings.
  keyword_to_response_dict = {
        "crashed": "Are the device drivers up to date?",
        "blue": "Ah, the blue screen! And then what happened?",
        "hacked": "You should consider installing anti-virus software.",
        "bluetooth": "The solution is as simple as enabling it.",
        "windows": "Ah, I think I see your problem. What version?",
        "apple": "You do mean the computer kind of apple don't you?",
        "spam": "You should see if your mail client can filter messages.",
        "connection": "Contact your internet provider."
    }
  
  # Display the welcome message to the user.
  print("Welcome to the automated technical support system.")
  print("Please describe your problem")

  # Main loop to keep getting user queries until "quit" is entered
  while True:
    # Get the user's query and convert it to lowercase for case-insensitive comparison.
    user_query = input().lower()

    # Exit if the user inputs "quit"
    if user_query == "quit":
      break

    # Split the user's query into individual words for keyword checking.
    query_words = user_query.split()

    # Flag to check if we found a matching keyword in the user's query.
    keyword_found = False

    # iterate over each word in the user's query
    for word in query_words:
      # if the word matches a keyboard in our dictionary.
      if word in keyword_to_response_dict:
        # Print the associated response and set the keyword flag to True.
        print(keyword_to_response_dict[word])
        keyword_found = True
        break # Break out of loop
      
    if not keyword_found:
      print("Please tell me more about your issue.")

automated_technical_support()