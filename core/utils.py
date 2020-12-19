import json


def read_json(name_json):
    with open(name_json, 'r', encoding='utf-8') as f:
        return json.load(f, )


if __name__ == '__main__':
    from models import Profile, Post, Comment

    db = read_json('db.json')

    users = db.get('users')
    posts = db.get('posts')
    comments = db.get('comments')

    for user in users:
        p = Profile(id=user.get('id'), name=user.get('name'), email=user.get('email'), street=user.get('address').get('street'), suite=user.get('address').get('suite'), city=user.get('address').get('city'), zipcode=user.get('address').get('zipcode'))
        p.save()

    for post in posts:
        p = Post(id=post.get('id'), title=post.get('title'), body=post.get('body'), userId=Profile.objects.get(id=post.get('userId')))
        p.save()

    for comment in comments:
        c = Comment(id=comment.get('id'), name=comment.get('name'), email=comment.get('email'), body=comment.get('body'), postId=Post.objects.get(id=comment.get('postId')))
        c.save()
