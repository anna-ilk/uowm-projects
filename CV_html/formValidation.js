document.getElementById('contactForm').addEventListener('submit', function(event) {
    // Ανάκτηση τιμών από τα πεδία
    const name = document.querySelector('input[name="fullname"]').value.trim();
    const email = document.querySelector('input[name="email"]').value.trim();
    const message = document.querySelector('textarea[name="message"]').value.trim();

    // Έλεγχος email
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // Έλεγχοι για κενά πεδία και μορφή email
    if (!name) {
        alert('Please enter your full name.');
        event.preventDefault(); // Αποτρέπουμε την αποστολή αν λείπει το όνομα
        return;
    }

    if (!email) {
        alert('Please enter your email address.');
        event.preventDefault(); // Αποτρέπουμε την αποστολή αν λείπει το email
        return;
    }

    if (!emailPattern.test(email)) {
        alert('Please enter a valid email address.');
        event.preventDefault(); // Αποτρέπουμε την αποστολή αν το email δεν είναι έγκυρο
        return;
    }

    if (!message) {
        alert('Please enter your message.');
        event.preventDefault(); // Αποτρέπουμε την αποστολή αν λείπει το μήνυμα
        return;
    }

    // Απόκρυψη φόρμας και εμφάνιση μηνύματος ευχαριστίας
    document.getElementById('contactForm').style.display = 'none';
    document.getElementById('thankYouMessage').style.display = 'block';

    // Επαναφόρτωση της σελίδας μετά από 5 δευτερόλεπτα
    setTimeout(function() {
        location.reload();
    }, 5000);
});
