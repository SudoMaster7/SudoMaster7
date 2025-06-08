import 'package:flutter/material.dart';
import 'package:sudo_aprender_brincar/screens/onboarding/create_profile_screen.dart';
import 'package:sudo_aprender_brincar/services/auth_service.dart';
import 'package:sudo_aprender_brincar/screens/lobby/lobby_screen.dart';
// Import other necessary screens for navigation, e.g., LobbyScreen, CreateProfileScreen

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final AuthService _authService = AuthService();
  final _formKey = GlobalKey<FormState>();
  String _email = '';
  String _password = '';
  String _errorMessage = '';
  bool _isLoading = false;

  void _tryLogin() async {
    if (_formKey.currentState!.validate()) {
      _formKey.currentState!.save();
      setState(() {
        _isLoading = true;
        _errorMessage = '';
      });
      try {
        final userCredential = await _authService.signInWithEmailAndPassword(_email, _password);
        if (userCredential != null && userCredential.user != null) {
          // Navigate to Lobby or Profile Creation if no profile exists
          // For MVP, let's assume navigation to a placeholder LobbyScreen
          Navigator.of(context).pushReplacement(MaterialPageRoute(builder: (_) => const LobbyScreen()));
           ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text('Login Successful! (MVP: Navigate to Lobby)')),
          );
        } else {
          setState(() {
            _errorMessage = 'Login failed. Please check your credentials.';
          });
        }
      } catch (e) {
        setState(() {
          _errorMessage = 'An error occurred: ${e.toString()}';
        });
      } finally {
        setState(() {
          _isLoading = false;
        });
      }
    }
  }

  void _tryRegister() async {
    if (_formKey.currentState!.validate()) {
      _formKey.currentState!.save();
      setState(() {
        _isLoading = true;
        _errorMessage = '';
      });
      try {
        final userCredential = await _authService.registerWithEmailAndPassword(_email, _password);
        if (userCredential != null && userCredential.user != null) {
          // Navigate to CreateProfileScreen
          // Navigator.of(context).pushReplacement(MaterialPageRoute(builder: (_) => CreateProfileScreen(parentUid: userCredential.user!.uid)));
           ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(content: Text('Registration Successful! UID: ${userCredential.user!.uid} (MVP: Navigate to Create Profile)')),
          );
        } else {
          setState(() {
            _errorMessage = 'Registration failed.';
          });
        }
      } catch (e) {
        setState(() {
          _errorMessage = 'An error occurred during registration: ${e.toString()}';
        });
      } finally {
        setState(() {
          _isLoading = false;
        });
      }
    }
  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Parent Login/Register')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              TextFormField(
                decoration: const InputDecoration(labelText: 'Email'),
                keyboardType: TextInputType.emailAddress,
                validator: (value) => value!.isEmpty || !value.contains('@') ? 'Invalid email' : null,
                onSaved: (value) => _email = value!,
              ),
              TextFormField(
                decoration: const InputDecoration(labelText: 'Password'),
                obscureText: true,
                validator: (value) => value!.isEmpty || value.length < 6 ? 'Password too short' : null,
                onSaved: (value) => _password = value!,
              ),
              const SizedBox(height: 20),
              if (_isLoading)
                const CircularProgressIndicator()
              else ...[
                ElevatedButton(
                  onPressed: _tryLogin,
                  child: const Text('Login'),
                ),
                TextButton(
                  onPressed: _tryRegister, // Placeholder for navigation to register screen or combined logic
                  child: const Text('Register New Account'),
                ),
              ],
              if (_errorMessage.isNotEmpty)
                Padding(
                  padding: const EdgeInsets.only(top: 10.0),
                  child: Text(
                    _errorMessage,
                    style: const TextStyle(color: Colors.red),
                    textAlign: TextAlign.center,
                  ),
                ),
            ],
          ),
        ),
      ),
    );
  }
}
