import google.generativeai as genai

def get_keyword_for_query(user_query):
    """
    Takes a user's query, generates a prompt requesting the generative model to return
    only the keyword associated with the user's intent based on a list of available services.
    """
    # Complete list of services
    services = [
        {"name": "Object Detection", "keyword": "كشف-الأشياء"},
        {"name": "Face Recognition", "keyword": "التعرف-على-الوجه"},
        {"name": "Time (Hijri, Gregorian)", "keyword": "معرفة-الوقت"},
        {"name": "Date", "keyword": "معرفة-التاريخ"},
        {"name": "Weather", "keyword": "حالة-الطقس"},
        {"name": "Media from YouTube", "keyword": "ميديا-من-يوتيوب"},
        {"name": "Search Wikipedia", "keyword": "بحث-ويكيبيديا"},
        {"name": "Playing Qur'an", "keyword": "تشغيل-القرآن"},
        {"name": "Status of Light of the Place", "keyword": "حالة-الإضاءة"},
        {"name": "Image Description on Gemini", "keyword": "وصف-الصورة"},
        {"name": "Translation and Optical Character Recognition (OCR)", "keyword": "الترجمة-والتعرف-الضوئي-على-الحروف"},
        {"name": "Send Messages on Telegram", "keyword": "إرسال-رسائل-تلغرام"},
        {"name": "Messenger Calls", "keyword": "مكالمات-الماسنجر"},
    ]
    
    # Generate a prompt focusing on keywords
    services_keywords = ', '.join([service['keyword'] for service in services])
    prompt = f"Given the user's query and the available services keywords: {services_keywords}, please return only the most appropriate keyword that matches the user's intent."
    
    # Combine the prompt with the user's query
    full_prompt = f"{prompt} User's query: \"{user_query}\""
    
    # Configuration for the Gemini API
    api_key = 'AIzaSyCHyeW-T_9nEo8H3NMiaCcqcZHn0Stq1pE'  # Replace with your actual API key
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    
    # Sending the combined prompt to the model
    response = model.generate_content(full_prompt)
    
    # Print the model's response
    return response.text

# Example usage
user_query = " مين ده "  # Example user query
response_keyword = get_keyword_for_query(user_query)
print(response_keyword)
