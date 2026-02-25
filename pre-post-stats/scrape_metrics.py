"""
Scrape pre-campaign Instagram metrics for 6 merchants.
Uses instaloader to pull public profile data and recent post engagement.
"""
import instaloader
import json
import time
import sys

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

MERCHANTS = [
    {"name": "Burger Bun", "handle": "burgerbunla"},
    {"name": "Chelo", "handle": "tasteofchelo"},
    {"name": "Falafel Corner", "handle": "falafelcornerdowntown"},
    {"name": "La Cocina", "handle": "lacocina_nj"},
    {"name": "Tee Jayes Country Place", "handle": "teejayescountryplace"},
    {"name": "Thai Cortez", "handle": "thai.cortez"},
]

MAX_POSTS_TO_ANALYZE = 12  # last 12 posts for averages

results = []

for mx in MERCHANTS:
    handle = mx["handle"]
    name = mx["name"]
    print(f"\n{'='*60}")
    print(f"Scraping: {name} (@{handle})")
    print(f"{'='*60}")

    try:
        profile = instaloader.Profile.from_username(L.context, handle)

        data = {
            "name": name,
            "handle": f"@{handle}",
            "followers": profile.followers,
            "following": profile.followees,
            "total_posts": profile.mediacount,
            "is_verified": profile.is_verified,
            "is_business": profile.is_business_account,
            "bio": profile.biography[:100] if profile.biography else "",
        }

        print(f"  Followers: {profile.followers}")
        print(f"  Following: {profile.followees}")
        print(f"  Total Posts: {profile.mediacount}")

        # Scrape recent posts for engagement metrics
        likes_list = []
        comments_list = []
        post_dates = []
        video_count = 0
        carousel_count = 0
        image_count = 0

        print(f"  Analyzing last {MAX_POSTS_TO_ANALYZE} posts...")
        for i, post in enumerate(profile.get_posts()):
            if i >= MAX_POSTS_TO_ANALYZE:
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

            # Small delay to avoid rate limiting
            if i > 0 and i % 5 == 0:
                time.sleep(1)

        posts_analyzed = len(likes_list)
        if posts_analyzed > 0:
            avg_likes = sum(likes_list) / posts_analyzed
            avg_comments = sum(comments_list) / posts_analyzed
            total_engagement = sum(likes_list) + sum(comments_list)
            avg_engagement_per_post = total_engagement / posts_analyzed
            engagement_rate = (avg_engagement_per_post / profile.followers * 100) if profile.followers > 0 else 0

            data["posts_analyzed"] = posts_analyzed
            data["avg_likes"] = round(avg_likes, 1)
            data["avg_comments"] = round(avg_comments, 1)
            data["avg_engagement_per_post"] = round(avg_engagement_per_post, 1)
            data["engagement_rate"] = round(engagement_rate, 2)
            data["max_likes"] = max(likes_list)
            data["min_likes"] = min(likes_list)
            data["video_count"] = video_count
            data["carousel_count"] = carousel_count
            data["image_count"] = image_count
            data["newest_post"] = post_dates[0] if post_dates else None
            data["oldest_analyzed"] = post_dates[-1] if post_dates else None

            print(f"\n  --- Summary ---")
            print(f"  Avg Likes: {avg_likes:.1f}")
            print(f"  Avg Comments: {avg_comments:.1f}")
            print(f"  Engagement Rate: {engagement_rate:.2f}%")
            print(f"  Best Post: {max(likes_list)} likes")
            print(f"  Content Mix: {video_count} videos, {carousel_count} carousels, {image_count} images")
        else:
            data["posts_analyzed"] = 0
            data["avg_likes"] = 0
            data["avg_comments"] = 0
            data["engagement_rate"] = 0
            print("  No posts found to analyze.")

        results.append(data)

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"  ERROR: Profile @{handle} not found")
        results.append({"name": name, "handle": f"@{handle}", "error": "Profile not found"})
    except instaloader.exceptions.ConnectionException as e:
        print(f"  ERROR: Connection issue for @{handle}: {e}")
        results.append({"name": name, "handle": f"@{handle}", "error": str(e)})
    except Exception as e:
        print(f"  ERROR: {type(e).__name__}: {e}")
        results.append({"name": name, "handle": f"@{handle}", "error": str(e)})

    # Delay between merchants to avoid rate limiting
    time.sleep(2)

# Save results as JSON
output_path = "/Users/vickie.hua/Documents/doordash-projects/social-media/pre_campaign_metrics.json"
with open(output_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\n\nResults saved to: {output_path}")

# Print summary table
print("\n" + "="*120)
print("PRE-CAMPAIGN INSTAGRAM SNAPSHOT (Feb 2026)")
print("="*120)
print(f"{'Merchant':<25} {'Handle':<25} {'Followers':>10} {'Posts':>8} {'Avg Likes':>10} {'Avg Comments':>13} {'Eng Rate':>10} {'Best Post':>10}")
print("-"*120)
for r in results:
    if "error" in r:
        print(f"{r['name']:<25} {r['handle']:<25} {'ERROR':>10}")
    else:
        print(f"{r['name']:<25} {r['handle']:<25} {r['followers']:>10,} {r['total_posts']:>8} {r.get('avg_likes', 0):>10.1f} {r.get('avg_comments', 0):>13.1f} {r.get('engagement_rate', 0):>9.2f}% {r.get('max_likes', 0):>10}")
print("="*120)
