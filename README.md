1.	Authentication Header (AH) and Encapsulating Security Payload:
•	Greek Text Input
•	"Γειά σου Κόσμε" ("Hello World" in Greek) is encoded with ISO-8859-7, a Greek character encoding.
•	Key & IV Generation
•	os.urandom(16) creates a 128-bit AES key and a 16-byte Initialization Vector (IV).
•	Encryption (ESP-like functionality)
•	AES in CFB mode is used for encryption.
•	The plaintext is transformed into ciphertext.
•	Integrity Check (AH-like functionality)
•	An HMAC with SHA-256 is computed over the ciphertext using the same key.
•	This produces an authentication tag that verifies data integrity.
•	Output
•	Original Greek text, encoded bytes, ciphertext, and authentication tag are printed.

2.	RFC 5322:
•	RFC5322 Regex
•	The pattern RFC5322_REGEX ensures:
	The local part (before @) doesn’t start or end with a dot.
	It allows alphanumeric characters and common symbols (.!#$%&'*+/=?^_{|}~-`).
	The domain part (after @) must be valid, with optional subdomains.
•	is_valid_email(email) function
•	Uses Python’s re.match() to check if the given email matches the regex.
•	Returns True if valid, False otherwise.
•	Test Cases
•	"example@example.com" ✅ Valid
•	"user.name+tag+sorting@example.com" ✅ Valid
•	"user@sub.example.com" ✅ Valid
•	"invalid-email@.com" ❌ Invalid (domain starts with a dot)
•	"another.invalid@domain..com" ❌ Invalid (double dot in domain)
•	Output
•	Prints whether each email is Valid or Invalid.

3. PKIX (Public Key Infrastructure X.509):
•	Import Libraries
•	cryptography.x509 for handling certificates.
•	default_backend() provides cryptographic backends.
•	Load the Certificate File
•	Opens certificate.pem (a certificate in PEM format).
•	Reads the raw bytes into cert_data.
•	Parse the Certificate
•	x509.load_pem_x509_certificate(cert_data, default_backend()) converts the PEM file into a usable certificate object.
•	Extract and Print Certificate Details
•	Subject → The entity the certificate belongs to (e.g., domain or person).
•	Issuer → The Certificate Authority (CA) that issued it.
•	Serial Number → A unique identifier for the certificate.
•	Validity Period → The time frame when the certificate is valid (not_valid_before → not_valid_after).



4.	Static Biometric:
•	File Upload
•	files.upload() lets you upload reference_signature.jpg and user_signature.jpg into Colab.
•	os.listdir() confirms the uploaded files.
•	Libraries
•	cv2 (OpenCV) for image processing.
•	numpy for array handling.
•	skimage.metrics.ssim for computing the similarity score.
•	compare_signatures(reference_path, user_path) Function
•	Loads both images in grayscale (cv2.imread(..., 0)).
•	Checks if images were loaded successfully.
•	Resizes both images to 300×300 for uniform comparison.
•	Computes SSIM score → a value between -1 and 1 (closer to 1 = more similar).
•	Compares score against a threshold of 0.8:
	≥ 0.8 → "Authentication Successful"
	< 0.8 → "Authentication Failed"

5.	One-Time Password (OTP):
   •	Kerberos Authentication (kerberos_authenticate)
•	Uses the kerberos library for GSSAPI-based authentication.
•	Steps:
	authGSSServerInit(service_name) → Initializes a Kerberos server context for a given service (e.g., HTTP@your-server-name).
	authGSSServerStep(context, "") → Processes the authentication step (in real use, this would include a client token).
	authGSSServerUserName(context) → Retrieves the authenticated Kerberos username.
	authGSSServerClean(context) → Cleans up the context after use.
•	If authentication fails, it catches a GSSError and prints the failure reason.
•	OTP Generation (generate_otp)
•	Creates a numeric OTP (default length = 6 digits).
•	Randomly selects digits between 0–9 and concatenates them into a string.
•	Prints the OTP for the user.


6.	TLS (Transport Layer Security):
•	SSL Connection with socket + ssl
•	Defines a server (example.com) and port (443, the default for HTTPS).
•	Creates a TCP connection with socket.create_connection.
•	Wraps the socket with SSL/TLS using ssl.create_default_context().
•	Prints the peer certificate (getpeercert()), showing details about the server’s SSL certificate.
•	HTTPS Request with requests
•	Sends a GET request to https://example.com.
•	The verify=True flag ensures that SSL certificates are validated (protecting against MITM attacks).
•	Prints the HTTP response status code (e.g., 200 for OK).
•	Prints the response body (HTML of the page).


