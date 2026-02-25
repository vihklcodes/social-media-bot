"""Scrape @falafelcorner_main to replace the downtown handle stats."""
import instaloader
import json
import time

L = instaloader.Instaloader(
    download_pictures=False,
    download_videos=False,
    download_video_thumbnails=False,
    download_geotags=False,
    download_comments=False,
    save_metadata=False,
    compress_json=False,
    quiet=True,
)

handle = "falafelcorner_main"
MAX_POSTS = 12

print(f"Scraping @{handle}...")
profile = instaloader.Profile.from_username(L.context, handle)

print(f"  Followers: {profile.followers}")
print(f"  Following: {profile.followees}")
print(f"  Total Posts: {profile.mediacount}")

likes_list = []
comments_list = []
post_dates = []
video_count = 0
carousel_count = 0
image_count = 0

for i, post in enumerate(profile.get_posts()):
    if i >= MAX_POSTS:
        break
    likes_list.append(post.likes)
    comments_list.append(post.comments)
    post_dates.append(post.date_utc.isoformat())
    if post.is_video:
        video_count += 1
    elif post.mediacount > 1:
        carousel_count += 1
    else:
        image_count += 1
    print(f"    Post {i+1}: {post.likes} likes, {post.comments} comments ({post.date_utc.strftime('%Y-%m-%d')})")
    if i > 0 and i % 5 == 0:
        time.sleep(1)

posts_analyzed = len(likes_list)
avg_likes = sum(likes_list) / posts_analyzed if posts_analyzed else 0
avg_comments = sum(comments_list) / posts_analyzed if posts_analyzed else 0
avg_eng = (avg_likes + avg_comments)
eng_rate = (avg_eng / profile.followers * 100) if profile.followers > 0 else 0

print(f"\n  Avg Likes: {avg_likes:.1f}")
print(f"  Avg Comments: {avg_comments:.1f}")
print(f"  Engagement Rate: {eng_rate:.2f}%")
print(f"  Best Post: {max(likes_list)} likes")
print(f"  Content Mix: {video_count} videos, {carousel_count} carousels, {image_count} images")
print(f"  Newest: {post_dates[0] if post_dates else 'N/A'}")
print(f"  Oldest analyzed: {post_dates[-1] if post_dates else 'N/A'}")
