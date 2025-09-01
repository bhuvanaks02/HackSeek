# HackSeek 🔍

**AI-Powered Global Hackathon Finder**

HackSeek is a full-stack web application that helps developers discover hackathons worldwide through intelligent filtering and AI-powered chatbot assistance. Find hackathons that match your location, date preferences, skill level, and interests.

## 🌟 Features

### Core Features
- **Smart Search**: Filter hackathons by location, date, prize money, and themes
- **AI Chatbot**: Natural language queries to find perfect hackathons
- **Global Coverage**: Scrapes hackathons from major platforms worldwide
- **Real-time Updates**: Automated scraping keeps data fresh
- **Calendar Integration**: Export hackathons to Google Calendar

### Data Sources
- **Hackathon Platforms**: Devpost, Unstop, Devfolio, MLH, HackerEarth
- **Event Platforms**: Luma, Eventbrite, Meetup
- **Social Media**: Twitter/X hackathon announcements
- **Tech Communities**: Reddit, Discord, Slack communities

## 🏗️ Architecture

**Frontend**: Next.js + React + TypeScript  
**Backend**: Python FastAPI + PostgreSQL  
**AI**: Claude API with local model fallback  
**Scraping**: Python + BeautifulSoup + Scrapy  
**Deployment**: Docker containers

## 📁 Project Structure

```
hackseek/
├── frontend/                 # Next.js React application
│   ├── src/
│   │   ├── components/       # Reusable UI components
│   │   ├── pages/           # Next.js pages
│   │   ├── hooks/           # Custom React hooks
│   │   ├── utils/           # Helper functions
│   │   └── styles/          # CSS modules & globals
│   ├── public/              # Static assets
│   └── package.json
│
├── backend/                 # FastAPI Python application
│   ├── app/
│   │   ├── api/            # API route handlers
│   │   ├── models/         # Database models
│   │   ├── services/       # Business logic
│   │   ├── utils/          # Helper functions
│   │   └── main.py         # FastAPI app entry point
│   ├── tests/              # Backend tests
│   └── requirements.txt
│
├── scraper/                # Web scraping modules
│   ├── scrapers/          # Individual site scrapers
│   │   ├── devpost.py
│   │   ├── unstop.py
│   │   ├── mlh.py
│   │   └── social_media.py
│   ├── utils/             # Scraping utilities
│   ├── scheduler.py       # Automated scraping jobs
│   └── main.py           # Scraper entry point
│
├── database/              # Database related files
│   ├── migrations/        # Database migrations
│   ├── schemas/          # SQL schema definitions
│   └── init.sql          # Initial database setup
│
├── docker-compose.yml    # Development environment
├── .env.example         # Environment variables template
└── README.md           # This file
```

## 🚀 Development Phases

### Phase 1: Foundation & Basic Scraping (Weeks 1-2)
**Goal**: Set up core infrastructure and basic hackathon data collection

#### Week 1: Project Setup
- [ ] Initialize Next.js frontend with TypeScript
- [ ] Set up FastAPI backend with basic routes
- [ ] Configure PostgreSQL database schema
- [ ] Docker development environment
- [ ] Basic CI/CD pipeline

#### Week 2: Core Data Collection
- [ ] Implement Devpost scraper
- [ ] Implement MLH scraper  
- [ ] Create database models for hackathons
- [ ] Basic API endpoints for hackathon data
- [ ] Simple frontend to display scraped hackathons

**Deliverable**: Working app that scrapes and displays hackathons from 2 major sources

### Phase 2: Enhanced Scraping & Search (Weeks 3-4)
**Goal**: Expand data sources and add filtering capabilities

#### Week 3: More Data Sources
- [ ] Unstop scraper implementation
- [ ] Devfolio scraper implementation
- [ ] HackerEarth scraper implementation
- [ ] Luma events scraper
- [ ] Data deduplication and normalization

#### Week 4: Search & Filtering
- [ ] Location-based filtering
- [ ] Date range filtering
- [ ] Theme/category filtering
- [ ] Prize money filtering
- [ ] Search functionality with pagination
- [ ] Improved frontend UI/UX

**Deliverable**: Comprehensive search interface with 5+ data sources

### Phase 3: AI Integration (Weeks 5-6)
**Goal**: Add intelligent chatbot and AI-powered recommendations

#### Week 5: AI Setup & Basic Chat
- [ ] Claude API integration with fallback models
- [ ] Basic chatbot interface
- [ ] Natural language query processing
- [ ] AI-powered hackathon matching
- [ ] Chat history and context management

#### Week 6: Smart Recommendations
- [ ] User preference learning
- [ ] Skill-based recommendations
- [ ] Difficulty level assessment
- [ ] Team size recommendations
- [ ] AI-generated hackathon summaries

**Deliverable**: Fully functional AI chatbot that understands hackathon queries

### Phase 4: Social Media & Advanced Features (Weeks 7-8)
**Goal**: Social media scraping and premium features

#### Week 7: Social Media Integration
- [ ] Twitter/X API integration
- [ ] Reddit API integration
- [ ] Social media hackathon detection
- [ ] Real-time social monitoring
- [ ] Community-driven submissions

#### Week 8: Advanced Features
- [ ] Google Calendar integration
- [ ] Email notifications system
- [ ] Hackathon bookmarking
- [ ] Export to ICS files
- [ ] Basic analytics dashboard

**Deliverable**: Complete feature set with social media integration

### Phase 5: User System & Personalization (Weeks 9-10)
**Goal**: User accounts and personalized experience

#### Week 9: Authentication System
- [ ] User registration/login
- [ ] JWT token management
- [ ] User profile management
- [ ] OAuth integration (Google, GitHub)
- [ ] Password reset functionality

#### Week 10: Personalization
- [ ] Personal hackathon history
- [ ] Custom notification preferences
- [ ] Saved searches and alerts
- [ ] Personalized AI recommendations
- [ ] User dashboard

**Deliverable**: Personalized user experience with accounts

### Phase 6: Production & Optimization (Weeks 11-12)
**Goal**: Production deployment and performance optimization

#### Week 11: Performance & Testing
- [ ] Comprehensive testing suite
- [ ] Performance optimization
- [ ] Database indexing and optimization
- [ ] Caching implementation
- [ ] Error handling and logging

#### Week 12: Deployment & Monitoring
- [ ] Production Docker setup
- [ ] Cloud deployment (Railway/Render/Vercel)
- [ ] Monitoring and alerting
- [ ] Backup strategies
- [ ] Documentation completion

**Deliverable**: Production-ready application with monitoring

## 🛠️ Quick Start

### Prerequisites
- Docker & Docker Compose
- Git

### Development Setup
```bash
# Clone the repository
git clone <your-repo-url>
cd hackseek

# Copy environment file
cp .env.example .env
# Edit .env with your API keys

# Start all services
docker-compose up -d

# Access the application
# Frontend: http://localhost:3000
# Backend: http://localhost:8000
# Database: localhost:5432
```

### Manual Setup (without Docker)
```bash
# Backend setup
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# Frontend setup
cd frontend
npm install
npm run dev

# Database setup
# Install PostgreSQL and create database
# Run migrations from database/migrations/
```

## 🔑 Environment Variables

Copy `.env.example` to `.env` and configure:

- **DATABASE_URL**: PostgreSQL connection string
- **CLAUDE_API_KEY**: Claude API key (or OpenAI as fallback)
- **TWITTER_BEARER_TOKEN**: For social media scraping
- **SMTP_**: Email notification settings

## 🤝 Contributing

This is a personal learning project, but suggestions and feedback are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

MIT License - see LICENSE file for details

## 🔮 Future Enhancements

- Mobile app development
- Advanced team matching
- Hackathon preparation resources
- Integration with coding platforms
- Hackathon outcome tracking
- Community features and forums

---

**Built with ❤️ for the hackathon community**
