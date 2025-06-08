import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:sudo_aprender_brincar/screens/onboarding/login_screen.dart';
// import 'package:sudo_aprender_brincar/services/auth_service.dart'; - May need later for auth state check
// import 'package:sudo_aprender_brincar/screens/lobby/lobby_screen.dart';

// Placeholder for Firebase options if not using flutterfire_cli
/*
const FirebaseOptions defaultFirebaseOptions = FirebaseOptions(
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_AUTH_DOMAIN",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_STORAGE_BUCKET",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
);
*/

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  // For actual Firebase setup, ensure you have the google-services.json / GoogleService-Info.plist
  // and run 'flutterfire configure' or manually set up.
  // The following line assumes Firebase is configured.
  try {
    // If you don't use flutterfire_cli, you might need to pass options:
    // await Firebase.initializeApp(options: defaultFirebaseOptions);
    await Firebase.initializeApp(); // Assumes flutterfire_cli or manual native setup done
  } catch (e) {
    print("Failed to initialize Firebase: $e");
    // Handle Firebase initialization error, maybe show an error screen
  }
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'SUDO Aprender & Brincar MVP',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      // For MVP, start with LoginScreen. Later, implement auth state checking.
      home: const LoginScreen(),
      // routes: {
      //   // Define routes for navigation if needed
      //   // '/lobby': (context) => LobbyScreen(),
      //   // '/create_profile': (context) => CreateProfileScreen(parentUid: ''), // This needs proper UID passing
      // },
    );
  }
}
