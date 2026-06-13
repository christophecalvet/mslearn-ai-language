from dotenv import load_dotenv
import os

# import namespaces
# import namespaces
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

#Troubleshoot
import traceback

def main():
    try:
        # Clear the console
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Get Configuration Settings
        load_dotenv()
        foundry_endpoint = os.getenv('FOUNDRY_ENDPOINT')
        agent_name = os.getenv('AGENT_NAME')
        

        # Get project client
        # Get project client
        project_client = AIProjectClient(
            endpoint=foundry_endpoint,
            credential=DefaultAzureCredential(),
        )        
        
        # Get an OpenAI client
        # Get an OpenAI client
        openai_client = project_client.get_openai_client()       
        
        # Main loop
        while True:
            # Get user input
            prompt = input("User prompt (or 'quit'): ")
            if prompt == "quit" or len(prompt) == 0:
                break
            else:
                # Use the agent to get a response
                # Use the agent to get a response
                response = openai_client.responses.create(
                    input=[{"role": "user", "content": prompt}],
                    extra_body={"agent_reference": {"name": agent_name, "type": "agent_reference"}},
                )

                print(response) # TROUBLESHOOT
                print(f"{agent_name}: {response.output_text}")               
                
    
    
            
    except Exception as ex:
        #print(ex) #Troubleshoot
        
        print("========== ERROR ==========")
        traceback.print_exc()
        print("Type:", type(ex))
        
        try:
            print("Args:", ex.args)
        except:
            pass


if __name__ == "__main__":
    main()