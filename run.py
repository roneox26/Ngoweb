import socket
from app import app, db, bcrypt, User, CashBalance

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        if not User.query.filter_by(email='admin@example.com').first():
            hashed_pw = bcrypt.generate_password_hash('admin123').decode('utf-8')
            admin = User(name='Admin', email='admin@example.com', password=hashed_pw, role='admin')
            db.session.add(admin)
        
        if not User.query.filter_by(email='staff@example.com').first():
            hashed_pw = bcrypt.generate_password_hash('staff123').decode('utf-8')
            staff = User(name='Staff', email='staff@example.com', password=hashed_pw, role='staff')
            db.session.add(staff)
        
        db.session.commit()
        
        if not CashBalance.query.first():
            initial_balance = CashBalance(balance=0)
            db.session.add(initial_balance)
            db.session.commit()
    
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    print("\n" + "="*60)
    print("NGO Management System Running...")
    print("="*60)
    print("\nAccess on this computer:")
    print("   http://localhost:5000")
    print(f"\nAccess from other devices on network:")
    print(f"   http://{local_ip}:5000")
    print("\nLogin Credentials:")
    print("   Admin: admin@example.com / admin123")
    print("   Staff: staff@example.com / staff123")
    print("\nPress Ctrl+C to stop")
    print("="*60 + "\n")
    
    app.run(host='0.0.0.0', port=5000, debug=False)
