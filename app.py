from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Portfolio</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        
        * {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        
        html {
            scroll-behavior: smooth;
        }
        
        body {
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            background: #0f0f14;
        }
        
        .sidebar {
            transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .sidebar-open {
            transform: translateX(0);
        }
        
        .sidebar-closed {
            transform: translateX(-100%);
        }
        
        .card-hover {
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .card-hover:hover {
            transform: translateY(-4px);
        }
        
        .nav-pill {
            transition: all 0.2s ease;
        }
        
        .nav-pill.active {
            background: rgba(255, 255, 255, 0.1);
            color: #fff;
        }
        
        .menu-item {
            transition: all 0.2s ease;
        }
        
        .menu-item:hover {
            background: rgba(255, 255, 255, 0.05);
            transform: translateX(4px);
        }
        
        .menu-item.active {
            background: rgba(139, 92, 246, 0.1);
            border-left: 3px solid rgb(139, 92, 246);
        }
        
        .page-content {
            display: none;
        }
        
        .page-content.active {
            display: block;
        }
        
        section {
            scroll-margin-top: 100px;
        }
    </style>
</head>
<body class="text-white">
    
    <!-- Sidebar -->
    <div id="sidebar" class="sidebar sidebar-closed fixed top-0 left-0 h-full w-64 bg-zinc-900/50 backdrop-blur-xl border-r border-zinc-800/50 z-50">
        <div class="p-6">
            <div class="flex items-center justify-between mb-8">
                <h2 class="text-xl font-bold">Menu</h2>
                <button onclick="toggleSidebar()" class="p-2 hover:bg-zinc-800 rounded-lg transition-colors">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                    </svg>
                </button>
            </div>
            
            <nav class="space-y-2">
                <button onclick="showPage('home')" class="menu-item active w-full flex items-center gap-3 px-4 py-3 rounded-lg text-left" data-page="home">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path>
                    </svg>
                    <span class="font-medium">Home</span>
                </button>
                
                <button onclick="showPage('projects')" class="menu-item w-full flex items-center gap-3 px-4 py-3 rounded-lg text-left text-gray-400" data-page="projects">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path>
                    </svg>
                    <span class="font-medium">Projects</span>
                </button>
                
                <button onclick="showPage('experience')" class="menu-item w-full flex items-center gap-3 px-4 py-3 rounded-lg text-left text-gray-400" data-page="experience">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                    </svg>
                    <span class="font-medium">Experience</span>
                </button>
                
                <button onclick="showPage('blog')" class="menu-item w-full flex items-center gap-3 px-4 py-3 rounded-lg text-left text-gray-400" data-page="blog">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path>
                    </svg>
                    <span class="font-medium">Blog</span>
                </button>
                
                <button onclick="showPage('resume')" class="menu-item w-full flex items-center gap-3 px-4 py-3 rounded-lg text-left text-gray-400" data-page="resume">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
                    </svg>
                    <span class="font-medium">Resume</span>
                </button>
            </nav>
            
            <div class="absolute bottom-6 left-6 right-6">
                <div class="p-4 bg-violet-500/10 rounded-xl border border-violet-500/20">
                    <p class="text-sm text-violet-300 mb-2">💡 Available for work</p>
                    <p class="text-xs text-gray-400">Open to new opportunities</p>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Overlay -->
    <div id="overlay" class="fixed inset-0 bg-black/50 backdrop-blur-sm z-40 hidden" onclick="toggleSidebar()"></div>
    
    <!-- Main Content -->
    <div class="min-h-screen">
        <!-- Top Navigation -->
        <nav class="fixed top-0 left-0 right-0 z-30 bg-zinc-900/30 backdrop-blur-xl border-b border-zinc-800/50">
            <div class="max-w-5xl mx-auto px-6 py-4">
                <div class="flex items-center justify-between">
                    <div class="flex items-center gap-4">
                        <button onclick="toggleSidebar()" class="p-2 hover:bg-zinc-800/50 rounded-lg transition-colors">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                            </svg>
                        </button>
                        <span class="text-xl font-bold">Portfolio</span>
                    </div>
                    <div id="home-nav" class="md:flex items-center gap-2 bg-zinc-900/50 rounded-full p-1.5">
                        <button onclick="scrollToSection('about')" class="nav-pill active px-5 py-2 rounded-full text-sm font-medium">
                            About
                        </button>
                        <button onclick="scrollToSection('skills')" class="nav-pill px-5 py-2 rounded-full text-sm font-medium text-gray-400">
                            Skills
                        </button>
                        <button onclick="scrollToSection('education')" class="nav-pill px-5 py-2 rounded-full text-sm font-medium text-gray-400">
                            Education
                        </button>
                        <button onclick="scrollToSection('contact')" class="nav-pill px-5 py-2 rounded-full text-sm font-medium text-gray-400">
                            Contact
                        </button>
                    </div>
                    <button id="back-home-btn" onclick="showPage('home')" class="hidden items-center gap-2 px-5 py-2 bg-zinc-900/50 rounded-full text-sm font-medium hover:bg-zinc-800/50 transition-colors">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
                        </svg>
                        Back to Home
                    </button>
                </div>
            </div>
        </nav>

        <!-- Home Page -->
        <div id="page-home" class="page-content active">
            <div class="pt-32 pb-20 px-6">
                <div class="max-w-5xl mx-auto space-y-12">
                    
                    <!-- About Section -->
                    <section id="about" class="pb-20">
                        <div class="space-y-8">
                            <div>
                                <div class="inline-block px-4 py-1.5 bg-zinc-800/50 rounded-full text-sm font-medium text-gray-300 mb-4">
                                    Welcome 👋
                                </div>
                                <h1 class="text-6xl md:text-7xl font-bold mb-4 leading-tight">
                                    Hi, I'm <span class="text-gray-400">Jan Jacek Wejchert</span>
                                </h1>
                                <p class="text-2xl text-gray-300 mb-2">Full Stack Developer</p>
                                <p class="text-lg text-gray-400">Based in Madrid, Spain</p>
                            </div>
                            
                            <div class="bg-zinc-900/30 backdrop-blur-xl rounded-3xl p-8 border border-zinc-800/50 card-hover">
                                <h2 class="text-2xl font-bold mb-4">About Me</h2>
                                <p class="text-gray-300 text-lg leading-relaxed">
                                    Passionate developer with expertise in building modern web applications. 
                                    I love creating intuitive user experiences and solving complex problems through elegant code.
                                    With a strong foundation in both frontend and backend technologies, I strive to deliver 
                                    high-quality solutions that make a difference. Passionate developer with expertise in building modern web applications. 
                                    I love creating intuitive user experiences and solving complex problems through elegant code.
                                    With a strong foundation in both frontend and backend technologies, I strive to deliver 
                                    high-quality solutions that make a difference. Passionate developer with expertise in building modern web applications. 
                                    I love creating intuitive user experiences and solving complex problems through elegant code.
                                    With a strong foundation in both frontend and backend technologies, I strive to deliver 
                                    high-quality solutions that make a difference. Passionate developer with expertise in building modern web applications. 
                                    I love creating intuitive user experiences and solving complex problems through elegant code.
                                    With a strong foundation in both frontend and backend technologies, I strive to deliver 
                                    high-quality solutions that make a difference. Passionate developer with expertise in building modern web applications. 
                                </p>
                            </div>
                        </div>
                    </section>

                    <!-- Skills Section -->
                    <section id="skills" class="pb-20">
                        <div class="space-y-8">
                            <div>
                                <h2 class="text-5xl font-bold mb-4">Technical Skills</h2>
                                <p class="text-gray-400 text-lg">Technologies and tools I work with</p>
                            </div>
                            
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div class="bg-zinc-900/30 backdrop-blur-xl rounded-3xl p-6 border border-zinc-800/50 card-hover">
                                    <div class="flex items-center gap-3 mb-4">
                                        <div class="w-12 h-12 bg-blue-500/10 rounded-2xl flex items-center justify-center">
                                            <svg class="w-6 h-6 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"></path>
                                            </svg>
                                        </div>
                                        <h3 class="text-xl font-bold">Programming & Analytical Languages</h3>
                                    </div>
                                    <div class="flex flex-wrap gap-2">
                                        <span class="px-3 py-1.5 bg-zinc-800/50 rounded-full text-sm text-gray-300">Python</span>
                                        <span class="px-3 py-1.5 bg-zinc-800/50 rounded-full text-sm text-gray-300">SQL</span>
                                        <span class="px-3 py-1.5 bg-zinc-800/50 rounded-full text-sm text-gray-300">R (RStudio</span>
                                        <span class="px-3 py-1.5 bg-zinc-800/50 rounded-full text-sm text-gray-300">Stata</span>
                                        <span class="px-3 py-1.5 bg-zinc-800/50 rounded-full text-sm text-gray-300">Mathematica</span>
                                    </div>
                                </div>
                                
                                <div class="bg-zinc-900/30 backdrop-blur-xl rounded-3xl p-6 border border-zinc-800/50 card-hover">
                                    <div class="flex items-center gap-3 mb-4">
                                        <div class="w-12 h-12 bg-green-500/10 rounded-2xl flex items-center justify-center">
                                            <svg class="w-6 h-6 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14M5 12a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v4a2 2 0 01-2 2M5 12a2 2 0 00-2 2v4a2 2 0 002 2h14a2 2 0 002-2v-4a2 2 0 00-2-2m-2-4h.01M17 16h.01"></path>
                                            </svg>
                                        </div>
                                        <h3 class="text-xl font-bold">Tools & Environments</h3>
                                    </div>
                                    <div class="flex flex-wrap gap-2">
                                        <span class="px-3 py-1.5 bg-zinc-800/50 rounded-full text-sm text-gray-300">Jupyter Notebokk</span>
                                        <span class="px-3 py-1.5 bg-zinc-800/50 rounded-full text-sm text-gray-300">PyCharm</span>
                                        <span class="px-3 py-1.5 bg-zinc-800/50 rounded-full text-sm text-gray-300">GitHub</span>
                                        <span class="px-3 py-1.5 bg-zinc-800/50 rounded-full text-sm text-gray-300">VS Code</span>
                                        <span class="px-3 py-1.5 bg-zinc-800/50 rounded-full text-sm text-gray-300">RStudio</span>
                                        <span class="px-3 py-1.5 bg-zinc-800/50 rounded-full text-sm text-gray-300">SQL development environments</span>
                                    </div>
                                </div>
                                
                                <div class="bg-zinc-900/30 backdrop-blur-xl rounded-3xl p-6 border border-zinc-800/50 card-hover">
                                    <div class="flex items-center gap-3 mb-4">
                                        <div class="w-12 h-12 bg-purple-500/10 rounded-2xl flex items-center justify-center">
                                            <svg class="w-6 h-6 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4"></path>
                                            </svg>
                                        </div>
                                        <h3 class="text-xl font-bold">Databases & Storage</h3>
                                    </div>
                                    <div class="flex flex-wrap gap-2">
                                        <span class="px-3 py-1.5 bg-zinc-800/50 rounded-full text-sm text-gray-300">Relational databases (DB2, MySQL)</span>
                                        <span class="px-3 py-1.5 bg-zinc-800/50 rounded-full text-sm text-gray-300">MongoDB</span>
                                        <span class="px-3 py-1.5 bg-zinc-800/50 rounded-full text-sm text-gray-300">HDFS & object storage (S3)</span>
                                        <span class="px-3 py-1.5 bg-zinc-800/50 rounded-full text-sm text-gray-300">Data lakes</span>
                                    </div>
                                </div>
                                
                                <div class="bg-zinc-900/30 backdrop-blur-xl rounded-3xl p-6 border border-zinc-800/50 card-hover">
                                    <div class="flex items-center gap-3 mb-4">
                                        <div class="w-12 h-12 bg-orange-500/10 rounded-2xl flex items-center justify-center">
                                            <svg class="w-6 h-6 text-orange-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path>
                                            </svg>
                                        </div>
                                        <h3 class="text-xl font-bold">Data Analysis & Modeling</h3>
                                    </div>
                                    <div class="flex flex-wrap gap-2">
                                        <span class="px-3 py-1.5 bg-zinc-800/50 rounded-full text-sm text-gray-300">Data cleaning & preparation</span>
                                        <span class="px-3 py-1.5 bg-zinc-800/50 rounded-full text-sm text-gray-300">Exploratory data analysis</span>
                                        <span class="px-3 py-1.5 bg-zinc-800/50 rounded-full text-sm text-gray-300">Time series analysis</span>
                                        <span class="px-3 py-1.5 bg-zinc-800/50 rounded-full text-sm text-gray-300">Forecasting</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>

                    <!-- Education Section -->
                    <section id="education" class="pb-20">
                        <div class="space-y-8">
                            <div>
                                <h2 class="text-5xl font-bold mb-4">Education</h2>
                                <p class="text-gray-400 text-lg">My academic background</p>
                            </div>
                            
                            <div class="space-y-4">
                                <div class="bg-zinc-900/30 backdrop-blur-xl rounded-3xl p-8 border border-zinc-800/50 card-hover">
                                    <div class="flex items-start justify-between flex-wrap gap-4">
                                        <div class="flex gap-4">
                                            <div class="w-12 h-12 bg-blue-500/10 rounded-2xl flex items-center justify-center flex-shrink-0">
                                                <svg class="w-6 h-6 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"></path>
                                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"></path>
                                                </svg>
                                            </div>
                                            <div>
                                                <h3 class="text-xl font-bold mb-1">Master of Science in Business Analytics and Data Science</h3>
                                                <p class="text-gray-300 mb-2">IE School of Science and Technology, Madrid, Spain</p>
                                                <p class="text-sm text-gray-400">Running GPA: 3,92 out of 4</p>
                                            </div>
                                        </div>
                                        <div class="px-4 py-2 bg-zinc-800/50 rounded-xl text-sm text-gray-300">
                                            2025 - 2026
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="bg-zinc-900/30 backdrop-blur-xl rounded-3xl p-8 border border-zinc-800/50 card-hover">
                                    <div class="flex items-start justify-between flex-wrap gap-4">
                                        <div class="flex gap-4">
                                            <div class="w-12 h-12 bg-purple-500/10 rounded-2xl flex items-center justify-center flex-shrink-0">
                                                <svg class="w-6 h-6 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"></path>
                                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"></path>
                                                </svg>
                                            </div>
                                            <div>
                                                <h3 class="text-xl font-bold mb-1">Bachelor of Science in Economics</h3>
                                                <p class="text-gray-300 mb-2">University of St Andrews, St Andrews, Scotland</p>
                                                <p class="text-sm text-gray-400">Graduated with Honours of the Second Class (Division l)</p>
                                            </div>
                                        </div>
                                        <div class="px-4 py-2 bg-zinc-800/50 rounded-xl text-sm text-gray-300">
                                            2021 - 2025
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="bg-zinc-900/30 backdrop-blur-xl rounded-3xl p-8 border border-zinc-800/50 card-hover">
                                    <div class="flex items-start justify-between flex-wrap gap-4">
                                        <div class="flex gap-4">
                                            <div class="w-12 h-12 bg-orange-500/10 rounded-2xl flex items-center justify-center flex-shrink-0">
                                                <svg class="w-6 h-6 text-orange-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"></path>
                                                </svg>
                                            </div>
                                            <div>
                                                <h3 class="text-xl font-bold mb-1">International A Levels</h3>
                                                <p class="text-gray-300 mb-2">Akademeia High School, Warsaw, Poland</p>
                                                <p class="text-sm text-gray-400">Economics, Mathematics, Further Mathematics, Polish (A*, A*, A*, A)</p>
                                            </div>
                                        </div>
                                        <div class="px-4 py-2 bg-zinc-800/50 rounded-xl text-sm text-gray-300">
                                            2019 - 2021
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>

                    <!-- Contact Section -->
                    <section id="contact" class="pb-20">
                        <div class="space-y-8">
                            <div>
                                <h2 class="text-5xl font-bold mb-4">Get In Touch</h2>
                                <p class="text-gray-400 text-lg">Let's connect and create something amazing together</p>
                            </div>
                            
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <a href="mailto:jan.wejchert@student.ie.edu" class="bg-zinc-900/30 backdrop-blur-xl rounded-3xl p-6 border border-zinc-800/50 card-hover block">
                                    <div class="flex items-center gap-4 mb-3">
                                        <div class="w-12 h-12 bg-blue-500/10 rounded-2xl flex items-center justify-center">
                                            <svg class="w-6 h-6 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                                            </svg>
                                        </div>
                                        <h3 class="text-xl font-bold">Email</h3>
                                    </div>
                                    <p class="text-gray-300">jan.wejchert@student.ie.edu</p>
                                </a>
                                
                                <a href="https://github.com/janwej" target="_blank" class="bg-zinc-900/30 backdrop-blur-xl rounded-3xl p-6 border border-zinc-800/50 card-hover block">
                                    <div class="flex items-center gap-4 mb-3">
                                        <div class="w-12 h-12 bg-purple-500/10 rounded-2xl flex items-center justify-center">
                                            <svg class="w-6 h-6 text-purple-400" fill="currentColor" viewBox="0 0 24 24">
                                                <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                                            </svg>
                                        </div>
                                        <h3 class="text-xl font-bold">GitHub</h3>
                                    </div>
                                    <p class="text-gray-300">github.com/janwej</p>
                                </a>
                                
                                <a href="https://linkedin.com/in/jan-wejchert" target="_blank" class="bg-zinc-900/30 backdrop-blur-xl rounded-3xl p-6 border border-zinc-800/50 card-hover block">
                                    <div class="flex items-center gap-4 mb-3">
                                        <div class="w-12 h-12 bg-green-500/10 rounded-2xl flex items-center justify-center">
                                            <svg class="w-6 h-6 text-green-400" fill="currentColor" viewBox="0 0 24 24">
                                                <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
                                            </svg>
                                        </div>
                                        <h3 class="text-xl font-bold">LinkedIn</h3>
                                    </div>
                                    <p class="text-gray-300">linkedin.com/in/jan-wejchert</p>
                                </a>
                                
                                <a href="https://twitter.com/yourusername" target="_blank" class="bg-zinc-900/30 backdrop-blur-xl rounded-3xl p-6 border border-zinc-800/50 card-hover block">
                                    <div class="flex items-center gap-4 mb-3">
                                        <div class="w-12 h-12 bg-cyan-500/10 rounded-2xl flex items-center justify-center">
                                            <svg class="w-6 h-6 text-cyan-400" fill="currentColor" viewBox="0 0 24 24">
                                                <path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z"/>
                                            </svg>
                                        </div>
                                        <h3 class="text-xl font-bold">Twitter</h3>
                                    </div>
                                    <p class="text-gray-300">@yourusername</p>
                                </a>
                            </div>
                        </div>
                    </section>

                </div>
            </div>
        </div>

        <!-- Projects Page -->
        <div id="page-projects" class="page-content">
            <div class="pt-32 pb-20 px-6">
                <div class="max-w-5xl mx-auto">
                    <div class="mb-12">
                        <h1 class="text-5xl font-bold mb-4">Projects</h1>
                        <p class="text-gray-400 text-lg">A showcase of my recent work and side projects</p>
                    </div>
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="bg-zinc-900/30 backdrop-blur-xl rounded-3xl overflow-hidden border border-zinc-800/50 card-hover">
                            <div class="h-48 bg-gradient-to-br from-blue-500/20 to-cyan-500/20 flex items-center justify-center">
                                <svg class="w-16 h-16 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path>
                                </svg>
                            </div>
                            <div class="p-6">
                                <div class="inline-block px-3 py-1 bg-blue-500/10 text-blue-400 rounded-full text-xs font-medium mb-3">
                                    E-Commerce
                                </div>
                                <h3 class="text-2xl font-bold mb-2">F1 Data Project</h3>
                                <p class="text-gray-400 mb-4">Fun project conducted for python class to play with f1 data set and to come up with some story from the given data</p>
                                <div class="flex flex-wrap gap-2 mb-4">
                                    <span class="px-3 py-1 bg-zinc-800/50 rounded-full text-xs text-gray-300">Comeback King</span>
                                    <span class="px-3 py-1 bg-zinc-800/50 rounded-full text-xs text-gray-300">Decade Champions</span>
                                    <span class="px-3 py-1 bg-zinc-800/50 rounded-full text-xs text-gray-300">Who will come out on top</span>
                                </div>
                                <button class="w-full px-4 py-2 bg-zinc-800/50 hover:bg-zinc-700/50 rounded-xl transition-colors">View Project</button>
                            </div>
                        </div>
                        
                        <div class="bg-zinc-900/30 backdrop-blur-xl rounded-3xl overflow-hidden border border-zinc-800/50 card-hover">
                            <div class="h-48 bg-gradient-to-br from-purple-500/20 to-pink-500/20 flex items-center justify-center">
                                <svg class="w-16 h-16 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path>
                                </svg>
                            </div>
                            <div class="p-6">
                                <div class="inline-block px-3 py-1 bg-purple-500/10 text-purple-400 rounded-full text-xs font-medium mb-3">
                                    AI/ML
                                </div>
                                <h3 class="text-2xl font-bold mb-2">Analytics Dashboard</h3>
                                <p class="text-gray-400 mb-4">Data visualization platform with machine learning insights for business intelligence.</p>
                                <div class="flex flex-wrap gap-2 mb-4">
                                    <span class="px-3 py-1 bg-zinc-800/50 rounded-full text-xs text-gray-300">Python</span>
                                    <span class="px-3 py-1 bg-zinc-800/50 rounded-full text-xs text-gray-300">TensorFlow</span>
                                    <span class="px-3 py-1 bg-zinc-800/50 rounded-full text-xs text-gray-300">D3.js</span>
                                </div>
                                <button class="w-full px-4 py-2 bg-zinc-800/50 hover:bg-zinc-700/50 rounded-xl transition-colors">View Project</button>
                            </div>
                        </div>
                        
                        <div class="bg-zinc-900/30 backdrop-blur-xl rounded-3xl overflow-hidden border border-zinc-800/50 card-hover">
                            <div class="h-48 bg-gradient-to-br from-green-500/20 to-emerald-500/20 flex items-center justify-center">
                                <svg class="w-16 h-16 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z"></path>
                                </svg>
                            </div>
                            <div class="p-6">
                                <div class="inline-block px-3 py-1 bg-green-500/10 text-green-400 rounded-full text-xs font-medium mb-3">
                                    Mobile
                                </div>
                                <h3 class="text-2xl font-bold mb-2">Social Media App</h3>
                                <p class="text-gray-400 mb-4">Mobile-first social platform with real-time messaging and personalized feeds.</p>
                                <div class="flex flex-wrap gap-2 mb-4">
                                    <span class="px-3 py-1 bg-zinc-800/50 rounded-full text-xs text-gray-300">React Native</span>
                                    <span class="px-3 py-1 bg-zinc-800/50 rounded-full text-xs text-gray-300">Firebase</span>
                                    <span class="px-3 py-1 bg-zinc-800/50 rounded-full text-xs text-gray-300">Redux</span>
                                </div>
                                <button class="w-full px-4 py-2 bg-zinc-800/50 hover:bg-zinc-700/50 rounded-xl transition-colors">View Project</button>
                            </div>
                        </div>
                        
                        <div class="bg-zinc-900/30 backdrop-blur-xl rounded-3xl overflow-hidden border border-zinc-800/50 card-hover">
                            <div class="h-48 bg-gradient-to-br from-orange-500/20 to-red-500/20 flex items-center justify-center">
                                <svg class="w-16 h-16 text-orange-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
                                </svg>
                            </div>
                            <div class="p-6">
                                <div class="inline-block px-3 py-1 bg-orange-500/10 text-orange-400 rounded-full text-xs font-medium mb-3">
                                    Performance
                                </div>
                                <h3 class="text-2xl font-bold mb-2">Real-Time Monitoring</h3>
                                <p class="text-gray-400 mb-4">System monitoring tool with real-time alerts and performance analytics.</p>
                                <div class="flex flex-wrap gap-2 mb-4">
                                    <span class="px-3 py-1 bg-zinc-800/50 rounded-full text-xs text-gray-300">Go</span>
                                    <span class="px-3 py-1 bg-zinc-800/50 rounded-full text-xs text-gray-300">WebSocket</span>
                                    <span class="px-3 py-1 bg-zinc-800/50 rounded-full text-xs text-gray-300">Docker</span>
                                </div>
                                <button class="w-full px-4 py-2 bg-zinc-800/50 hover:bg-zinc-700/50 rounded-xl transition-colors">View Project</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Experience Page -->
        <div id="page-experience" class="page-content">
            <div class="pt-32 pb-20 px-6">
                <div class="max-w-5xl mx-auto">
                    <div class="mb-12">
                        <h1 class="text-5xl font-bold mb-4">Experience</h1>
                        <p class="text-gray-400 text-lg">My professional journey</p>
                    </div>
                    
                    <div class="space-y-6">
                        <div class="bg-zinc-900/30 backdrop-blur-xl rounded-3xl p-8 border border-zinc-800/50 card-hover">
                            <div class="flex items-start justify-between flex-wrap gap-4 mb-4">
                                <div>
                                    <h3 class="text-2xl font-bold mb-2">Senior Full Stack Developer</h3>
                                    <p class="text-violet-400 font-medium mb-2">Tech Company Inc.</p>
                                    <p class="text-sm text-gray-400">Led development of microservices architecture and mentored junior developers</p>
                                </div>
                                <div class="px-4 py-2 bg-zinc-800/50 rounded-xl text-sm text-gray-300">
                                    2022 - Present
                                </div>
                            </div>
                            <div class="flex flex-wrap gap-2">
                                <span class="px-3 py-1 bg-zinc-800/50 rounded-full text-xs text-gray-300">React</span>
                                <span class="px-3 py-1 bg-zinc-800/50 rounded-full text-xs text-gray-300">Node.js</span>
                                <span class="px-3 py-1 bg-zinc-800/50 rounded-full text-xs text-gray-300">AWS</span>
                                <span class="px-3 py-1 bg-zinc-800/50 rounded-full text-xs text-gray-300">Docker</span>
                            </div>
                        </div>
                        
                        <div class="bg-zinc-900/30 backdrop-blur-xl rounded-3xl p-8 border border-zinc-800/50 card-hover">
                            <div class="flex items-start justify-between flex-wrap gap-4 mb-4">
                                <div>
                                    <h3 class="text-2xl font-bold mb-2">Full Stack Developer</h3>
                                    <p class="text-violet-400 font-medium mb-2">Startup XYZ</p>
                                    <p class="text-sm text-gray-400">Built customer-facing web applications and improved system performance by 40%</p>
                                </div>
                                <div class="px-4 py-2 bg-zinc-800/50 rounded-xl text-sm text-gray-300">
                                    2020 - 2022
                                </div>
                            </div>
                            <div class="flex flex-wrap gap-2">
                                <span class="px-3 py-1 bg-zinc-800/50 rounded-full text-xs text-gray-300">Vue.js</span>
                                <span class="px-3 py-1 bg-zinc-800/50 rounded-full text-xs text-gray-300">Python</span>
                                <span class="px-3 py-1 bg-zinc-800/50 rounded-full text-xs text-gray-300">PostgreSQL</span>
                            </div>
                        </div>
                        
                        <div class="bg-zinc-900/30 backdrop-blur-xl rounded-3xl p-8 border border-zinc-800/50 card-hover">
                            <div class="flex items-start justify-between flex-wrap gap-4 mb-4">
                                <div>
                                    <h3 class="text-2xl font-bold mb-2">Junior Developer</h3>
                                    <p class="text-violet-400 font-medium mb-2">Digital Agency</p>
                                    <p class="text-sm text-gray-400">Developed responsive websites and collaborated with design team</p>
                                </div>
                                <div class="px-4 py-2 bg-zinc-800/50 rounded-xl text-sm text-gray-300">
                                    2018 - 2020
                                </div>
                            </div>
                            <div class="flex flex-wrap gap-2">
                                <span class="px-3 py-1 bg-zinc-800/50 rounded-full text-xs text-gray-300">JavaScript</span>
                                <span class="px-3 py-1 bg-zinc-800/50 rounded-full text-xs text-gray-300">HTML/CSS</span>
                                <span class="px-3 py-1 bg-zinc-800/50 rounded-full text-xs text-gray-300">WordPress</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Blog Page -->
        <div id="page-blog" class="page-content">
            <div class="pt-32 pb-20 px-6">
                <div class="max-w-5xl mx-auto">
                    <div class="mb-12">
                        <h1 class="text-5xl font-bold mb-4">Blog</h1>
                        <p class="text-gray-400 text-lg">Thoughts, tutorials, and insights</p>
                    </div>
                    
                    <div class="grid grid-cols-1 gap-6">
                        <article class="bg-zinc-900/30 backdrop-blur-xl rounded-3xl p-8 border border-zinc-800/50 card-hover">
                            <div class="flex items-center gap-3 mb-4">
                                <span class="px-3 py-1 bg-blue-500/10 text-blue-400 rounded-full text-xs font-medium">Tutorial</span>
                                <span class="text-sm text-gray-400">Dec 15, 2024</span>
                            </div>
                            <h2 class="text-2xl font-bold mb-3">Building Scalable Microservices with Node.js</h2>
                            <p class="text-gray-400 mb-4">Learn how to architect and deploy microservices that can handle millions of requests...</p>
                            <button class="text-violet-400 hover:text-violet-300 font-medium">Read more →</button>
                        </article>
                        
                        <article class="bg-zinc-900/30 backdrop-blur-xl rounded-3xl p-8 border border-zinc-800/50 card-hover">
                            <div class="flex items-center gap-3 mb-4">
                                <span class="px-3 py-1 bg-purple-500/10 text-purple-400 rounded-full text-xs font-medium">Opinion</span>
                                <span class="text-sm text-gray-400">Dec 10, 2024</span>
                            </div>
                            <h2 class="text-2xl font-bold mb-3">The Future of Web Development in 2025</h2>
                            <p class="text-gray-400 mb-4">My thoughts on emerging trends and technologies that will shape web development...</p>
                            <button class="text-violet-400 hover:text-violet-300 font-medium">Read more →</button>
                        </article>
                        
                        <article class="bg-zinc-900/30 backdrop-blur-xl rounded-3xl p-8 border border-zinc-800/50 card-hover">
                            <div class="flex items-center gap-3 mb-4">
                                <span class="px-3 py-1 bg-green-500/10 text-green-400 rounded-full text-xs font-medium">Guide</span>
                                <span class="text-sm text-gray-400">Dec 5, 2024</span>
                            </div>
                            <h2 class="text-2xl font-bold mb-3">Complete Guide to React Performance Optimization</h2>
                            <p class="text-gray-400 mb-4">Practical tips and techniques to make your React applications lightning fast...</p>
                            <button class="text-violet-400 hover:text-violet-300 font-medium">Read more →</button>
                        </article>
                    </div>
                </div>
            </div>
        </div>

        <!-- Resume Page -->
        <div id="page-resume" class="page-content">
            <div class="pt-32 pb-20 px-6">
                <div class="max-w-5xl mx-auto">
                    <div class="mb-12 flex items-center justify-between flex-wrap gap-4">
                        <div>
                            <h1 class="text-5xl font-bold mb-4">Resume</h1>
                            <p class="text-gray-400 text-lg">Download or view my full resume</p>
                        </div>
                        <button class="px-6 py-3 bg-violet-500 hover:bg-violet-600 rounded-xl font-medium transition-colors flex items-center gap-2">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
                            </svg>
                            Download PDF
                        </button>
                    </div>
                    
                    <div class="bg-zinc-900/30 backdrop-blur-xl rounded-3xl p-12 border border-zinc-800/50">
                        <div class="space-y-8">
                            <div class="text-center">
                                <h2 class="text-4xl font-bold mb-2">Your Name</h2>
                                <p class="text-xl text-gray-300 mb-4">Full Stack Developer</p>
                                <div class="flex flex-wrap items-center justify-center gap-6 text-sm text-gray-400">
                                    <span>📧 your.email@example.com</span>
                                    <span>📍 Madrid, Spain</span>
                                    <span>🌐 yourwebsite.com</span>
                                </div>
                            </div>
                            
                            <div class="border-t border-zinc-800 pt-8">
                                <h3 class="text-2xl font-bold mb-4">Professional Summary</h3>
                                <p class="text-gray-300 leading-relaxed">
                                    Experienced Full Stack Developer with 5+ years of expertise in building scalable web applications. 
                                    Proficient in modern JavaScript frameworks, cloud technologies, and agile methodologies. 
                                    Passionate about creating efficient, user-centric solutions that drive business value.
                                </p>
                            </div>
                            
                            <div class="border-t border-zinc-800 pt-8">
                                <h3 class="text-2xl font-bold mb-4">Technical Skills</h3>
                                <div class="grid grid-cols-2 gap-4">
                                    <div>
                                        <h4 class="font-semibold text-gray-300 mb-2">Frontend</h4>
                                        <p class="text-gray-400 text-sm">React, TypeScript, Next.js, Tailwind CSS, Vue.js</p>
                                    </div>
                                    <div>
                                        <h4 class="font-semibold text-gray-300 mb-2">Backend</h4>
                                        <p class="text-gray-400 text-sm">Node.js, Python, Express, Django, REST APIs</p>
                                    </div>
                                    <div>
                                        <h4 class="font-semibold text-gray-300 mb-2">Database</h4>
                                        <p class="text-gray-400 text-sm">PostgreSQL, MongoDB, Redis, MySQL</p>
                                    </div>
                                    <div>
                                        <h4 class="font-semibold text-gray-300 mb-2">DevOps</h4>
                                        <p class="text-gray-400 text-sm">Docker, AWS, CI/CD, Kubernetes</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>

    <script>
        let currentPage = 'home';
        let activeSection = 'about';
        
        function toggleSidebar() {
            const sidebar = document.getElementById('sidebar');
            const overlay = document.getElementById('overlay');
            
            if (sidebar.classList.contains('sidebar-closed')) {
                sidebar.classList.remove('sidebar-closed');
                sidebar.classList.add('sidebar-open');
                overlay.classList.remove('hidden');
            } else {
                sidebar.classList.add('sidebar-closed');
                sidebar.classList.remove('sidebar-open');
                overlay.classList.add('hidden');
            }
        }
        
        function showPage(page) {
            currentPage = page;
            
            // Hide all pages
            document.querySelectorAll('.page-content').forEach(p => {
                p.classList.remove('active');
            });
            
            // Show selected page
            document.getElementById('page-' + page).classList.add('active');
            
            // Update menu items
            document.querySelectorAll('.menu-item').forEach(item => {
                const itemPage = item.getAttribute('data-page');
                if (itemPage === page) {
                    item.classList.add('active');
                    item.classList.remove('text-gray-400');
                } else {
                    item.classList.remove('active');
                    item.classList.add('text-gray-400');
                }
            });
            
            // Show/hide home nav and back button
            const homeNav = document.getElementById('home-nav');
            const backBtn = document.getElementById('back-home-btn');
            if (page === 'home') {
                homeNav.classList.remove('hidden');
                homeNav.classList.add('md:flex');
                backBtn.classList.add('hidden');
                backBtn.classList.remove('md:flex');
            } else {
                homeNav.classList.add('hidden');
                homeNav.classList.remove('md:flex');
                backBtn.classList.remove('hidden');
                backBtn.classList.add('md:flex');
            }
            
            // Close sidebar
            const sidebar = document.getElementById('sidebar');
            const overlay = document.getElementById('overlay');
            sidebar.classList.add('sidebar-closed');
            sidebar.classList.remove('sidebar-open');
            overlay.classList.add('hidden');
            
            // Scroll to top
            window.scrollTo(0, 0);
        }
        
        function scrollToSection(section) {
            activeSection = section;
            document.getElementById(section)?.scrollIntoView({ behavior: 'smooth' });
            updateNavButtons();
        }
        
        function updateNavButtons() {
            const buttons = document.querySelectorAll('.nav-pill');
            buttons.forEach(btn => {
                const onclickStr = btn.getAttribute('onclick');
                const section = onclickStr.match(/'([^']+)'/)[1];
                if (section === activeSection) {
                    btn.className = 'nav-pill active px-5 py-2 rounded-full text-sm font-medium';
                } else {
                    btn.className = 'nav-pill px-5 py-2 rounded-full text-sm font-medium text-gray-400';
                }
            });
        }
        
        // Update active section based on scroll position
        const observerOptions = {
            root: null,
            rootMargin: '-50% 0px -50% 0px',
            threshold: 0
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && currentPage === 'home') {
                    activeSection = entry.target.id;
                    updateNavButtons();
                }
            });
        }, observerOptions);
        
        document.querySelectorAll('section').forEach(section => {
            observer.observe(section);
        });
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True)
