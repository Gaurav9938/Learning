import subprocess
import time
import os



def rsync(source_directory,destination_directory):
    rsync_command = [
        "rsync",
        "-u",  # Update files only
        "-r",  # Recursively copy directories
        "-v",  # Verbose output
        source_directory,
        destination_directory
    ]
    
    try:
        # Run the rsync command
        subprocess.run(rsync_command, check=True)
        print("rsync completed successfully")
    except subprocess.CalledProcessError as e:
        print(f"rsync failed with error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    

        
def check_updates(destination_path):
    source_directory = "/cygdrive/z/compilers/"+destination_path
    destination_path=destination_path.replace("/i486_nt/", "")
    ptc_compilers_path = os.environ.get('PTC_COMPILERS_ROOT')
    ptc_compilers_path = ptc_compilers_path.replace(":", "")
    destination_directory = "/cygdrive/"+ptc_compilers_path
   
    rsync(source_directory,destination_directory)
    
    
    

if __name__ == "__main__":
    start_t=time.time()
    
    variables = [
    "/i486_nt/sdk10",
    "/i486_nt/netfxsdk471",
    "/i486_nt/netfxsdk472",
    "/i486_nt/netfxsdk48",
    "/i486_nt/netfx472",
    "/i486_nt/vs16u4",
    "/i486_nt/vs16.7.5",
    "/i486_nt/vs16.9.8",
    "/i486_nt/sdk10.0.19041.0",
    "/i486_nt/vs17.6.5",
    "/i486_nt/sdk10.0.22621.755"
    ]

    for data in variables:

        destination_path = data.strip()
        check_updates(destination_path)
        print("Checked for ",destination_path)

    end_t=time.time()
    print("The total time taken is: ",(end_t-start_t)/60)
    
        