<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LOGICS ADS MEDIA</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #lightgreen;
            color: #blue;
        }
        header {
            background-color: #black;
            color: white;
            padding: 122px 0;
            text-align: center;
        }
        nav a {
            color: white;
            margin: 0 15px;
            text-decoration: none;
            font-weight: bold;
        }
        .hero {
            text-align: center;
            padding: 80px 20px;
            background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('https://source.unsplash.com/1600x600/?advertising,media');
            background-size: cover;
            background-position: center;
            color: white;
        }
        .hero h1 {
            font-size: 50px;
        }
        .content {
            padding: 40px 20px;
            max-width: 1000px;
            margin: auto;
        }
        .services {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }
        .service-card {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        footer {
            background-color: #white;
            color: white;
            text-align: center;
            padding: 15px 0;
            margin-top: 40px;
        }
    </style>
</head>
<body>

<header>
    <h1>LOGIC'S ADS MEDIA</h1>
    <nav>
        <a href="#services">Services</a>
        <a href="#about">About</a>
        <a href="#contact">Contact</a>
    </nav>
</header>

<section class="hero">
    <h1>Your Trusted Advertising Partner</h1>
    <p>We bring your brand to life with creative and impactful ad solutions.</p>
</section>

<section class="content" id="services">
    <h2>Our Services</h2>
    <div class="services">
        <div class="service-card">
            <h3>Digital Marketing</h3>
            <p>Boost your online presence with targeted campaigns across social media and Google Ads.</p>
        </div>
        <div class="service-card">
            <h3>Video Production</h3>
            <p>Engaging ad videos, promotional reels, and brand stories tailored for your audience.</p>
        </div>
        <div class="service-card">
            <h3>Graphic Design</h3>
            <p>Eye-catching creatives for banners, posters, social media, and more.</p>
        </div>
    </div>
</section>

<section class="content" id="about">
    <h2>About Us</h2>
    <p>LOGIC'S ADS MEDIA is a leading creative agency helping brands grow through powerful advertising and media solutions. We mix strategy with creativity to deliver impactful campaigns that get results.</p>
</section>

<section class="content" id="contact">
    <h2>Contact Us</h2>
    <p>Email: contact@logicsadsmedia.com</p>
    <p>Phone: +91-XXXXXXXXXX</p>
    <p>Address: Mumbai, India</p>
</section>

<footer>
    &copy; 2025 LOGIC'S ADS MEDIA | All Rights Reserved
</footer>

</body>
</html>
