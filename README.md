# Django Blog Project

A modern, responsive blog application built with Django, featuring user authentication, rich text editing, commenting system, and dark mode support.

## Features

- **User Authentication**: Registration, login, logout with secure password handling
- **Blog Management**: Create, view, edit, and manage blog posts with categories
- **User Profiles**: Update username, email, and personal information
- **Rich Text Editor**: TinyMCE integration for enhanced content creation
- **Commenting System**: Nested comments and replies on blog posts
- **Responsive Design**: Mobile-friendly UI with Tailwind CSS
- **Dark Mode**: Toggle between light and dark themes
- **Pagination**: Efficient post listing with pagination
- **Search Functionality**: Search posts by title, author, content, or category
- **Rate Limiting**: Protection against spam with django-ratelimit
- **SEO Friendly**: Slug-based URLs for better search engine optimization

## Tech Stack

- **Backend**: Django 5.0.1
- **Frontend**: HTML, Tailwind CSS, Alpine.js
- **Database**: SQLite (development), PostgreSQL/MySQL (production)
- **Rich Text Editor**: TinyMCE (requires API key)
- **Icons**: Font Awesome

## TinyMCE Setup

To use the rich text editor for blog posts, you need a TinyMCE API key:

1. Visit [TinyMCE Cloud](https://www.tiny.cloud/)
2. Sign up for a free account
3. Get your API key from the dashboard
4. Add it to your `.env` file: `TINYMCE_API_KEY=your-api-key-here`

Without an API key, TinyMCE will work in free mode with limited features.

## Prerequisites

- Python 3.10 or higher
- pip package manager

## Environment Setup

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd blog
   ```

2. **Create Environment File:**
   Create a `.env` file in the project root and add your configuration:
   ```bash
   # Django Blog Project Environment Variables

   # Django Secret Key (generate a new one for production)
   SECRET_KEY=your-secret-key-here

   # TinyMCE API Key (get from https://www.tiny.cloud/)
   TINYMCE_API_KEY=your-tinymce-api-key-here

   # Debug Mode
   DEBUG=True
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Create Superuser (Optional):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application:**
   Open your browser and go to `http://127.0.0.1:8000/`

## Usage

### Creating Posts
1. Log in to your account
2. Navigate to the Blogs page
3. Click "Create New Blog"
4. Fill in the title, content (using rich text editor), and select a category
5. Submit the post

### Editing Posts
- Only the author of a post can edit it
- Click "Edit Post" on your own posts
- Make changes and save

### Managing Profile
- Click on your username in the navigation
- Select "Profile" to update your information
- Change username, email, first name, last name
- View all your blog posts

### Commenting
- Users must be logged in to comment
- Click "Reply" under any post or comment to add replies
- Nested comments are supported

### Dark Mode
- Click the moon/sun icon in the navigation bar to toggle themes
- Theme preference is saved in localStorage

## Project Structure

```
blog/
├── blog/                    # Main blog app
│   ├── models.py           # Post and Comment models
│   ├── views.py            # View functions
│   ├── urls.py             # URL patterns
│   └── templates/blog/     # Blog templates
├── home/                   # Home app
│   ├── models.py          # Contact model
│   ├── views.py           # Home and contact views
│   └── templates/home/    # Home templates
├── django_project/         # Project settings
├── static/                 # Static files
├── templates/              # Base templates
└── requirements.txt        # Python dependencies
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For questions or issues, please open an issue on GitHub or contact the maintainers.
   ```
Acknowledgements<br>
Django: A high-level Python web framework that encourages rapid development.<br>
Tailwind CSS: A utility-first CSS framework for creating custom designs.<br>
Font Awesome: Provides scalable vector icons.
