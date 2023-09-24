from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import current_user, login_user, logout_user, login_required
from apps import app, db
from apps.models import Comment, User, Post
from apps.forms import PostForm
from werkzeug.security import generate_password_hash
from flask import abort



@app.route('/')
def index():

    return render_template('index.html')


@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if request.method == 'POST':
        print(User)
        content = form.content.data
        my_post = Post(content, current_user.id)
        
        db.session.add(my_post)  
        db.session.commit()
        return redirect(url_for('post_feed', post_success=True))

    return render_template('post.html', form=form)


@app.route('/post_feed', methods=['GET', 'POST'])
@login_required
def post_feed():
    form = PostForm()

    if request.method == 'POST' and form.validate_on_submit():
        content = form.content.data
        new_post = Post(content=content, author=current_user)
        db.session.add(new_post)
        db.session.commit()

    posts = Post.query.all()
    return render_template('post_feed.html', posts=posts, form=form)




@app.route('/comment/<int:post_id>', methods=['POST'])
def comment(post_id):
    comment_content = request.form.get('comment_content')
    post = Post.query.get_or_404(post_id)
    
    new_comment = Comment(content=comment_content, user=current_user)
    new_comment.associate_with_post(post)  
    db.session.add(new_comment)  
    db.session.commit()  
    
    return redirect(url_for('post_feed'))



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query')
    return render_template('search.html', query=query)



sample_user = {
    'username': 'example_user',
    'password': 'example_password',
}



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and password == '1234': 
            session['user_id'] = user.id
            session['logged_in'] = True
            login_user(user)
            return redirect(url_for('post_feed'))  
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')

if __name__ == '__main__':
    app.run()



@app.before_request
def require_login():
    if request.endpoint == 'post' and 'user_id' not in session and request.endpoint != 'login':
        return redirect(url_for('login'))




@app.route('/logout')
def logout():
    session.clear()  
    return redirect(url_for('home')) 




@app.route('/edit-profile', methods=['GET', 'POST'])
def edit_profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        
        user = get_user_by_id(session['user_id'])

        
        user.username = request.form['username']
        user.email = request.form['email']
        

       
        db.session.commit()

        flash('Profile updated successfully', 'success')
        return redirect(url_for('profile'))

    return render_template('edit_profile.html', user=current_user)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        hashed_password = generate_password_hash(password)  
        
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        session['user_id'] = new_user.id
        session['logged_in'] = True
        
        return redirect(url_for('profile'))
    
    return render_template('signup.html')

  

sample_user = {
    'username': 'example_user',
    'email': 'user@example.com',
    
}

def get_user_by_id(user_id):
    return User.query.get(user_id)

@app.route('/profile')
def profile():
    if session.get('logged_in'):
       
        user_id = session['user_id']
        
        
        user = get_user_by_id(user_id)
        
        if user:
            return render_template('profile.html', user=user)
        else:
         
            return render_template('error.html', message='User not found')
    else:
        
        return redirect(url_for('login'))




@app.route('/information')
def information():
    return render_template('information.html')

@app.route('/information2')
def information2():
    return render_template('information2.html')

@app.route('/information3')
def information3():
    return render_template('information3.html')


@app.route('/delete_post/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    
    
    if post.author == current_user:
        db.session.delete(post)
        db.session.commit()
    
    return redirect(url_for('post_feed'))

@app.route('/delete_comment/<int:comment_id>', methods=['POST'])
def delete_comment(comment_id):
    # Retrieve the comment by ID
    comment = Comment.query.get_or_404(comment_id)

    # Check if the current user has permission to delete the comment (you may want to implement this logic)
    if current_user != comment.user:
        abort(403)  # Forbidden

    # Delete the comment
    db.session.delete(comment)
    db.session.commit()

    # Redirect to the post page or wherever you want to go after comment deletion
    return redirect(url_for('post_detail', post_id=comment.post.id))
