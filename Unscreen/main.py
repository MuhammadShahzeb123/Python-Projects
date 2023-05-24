import requests
import argparse

endpoint = "https://api.unscreen.com/v1.0/videos"

parser = argparse.ArgumentParser(description='Upload video to Unscreen')
parser.add_argument('video_path', metavar='video_path', type=str,
                    help='path to the video file')
args = parser.parse_args()

api_key = "Hd9wVVcktm4jiici4TbRGG17"
video_file = {'video_file': open(args.video_path, 'rb')}

response = requests.post(endpoint, headers={"X-Api-Key": api_key}, files=video_file)

video_id = response.json()["data"]["id"]

response = requests.get(f"{endpoint}/{video_id}", headers={"X-Api-Key": api_key})

print(response.json())