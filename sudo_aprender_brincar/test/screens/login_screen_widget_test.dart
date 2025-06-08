import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:sudo_aprender_brincar/main.dart'; // To initialize app for context
import 'package:sudo_aprender_brincar/screens/onboarding/login_screen.dart';
// Mock Firebase initialization if needed, or ensure it's handled (e.g. by importing MyApp)

void main() {
  // It's good practice to ensure Firebase is initialized for widget tests if they depend on it.
  // However, for pure UI widget tests, you might not need full Firebase.
  // For this MVP, we'll wrap with a MaterialApp.

  // Helper to pump LoginScreen with MaterialApp
  Future<void> pumpLoginScreen(WidgetTester tester) async {
    // A common pattern is to have a common test_helper.dart to initialize app / firebase for tests
    // For now, simple MaterialApp wrapper.
    // If Firebase.initializeApp() is called in LoginScreen or its dependencies,
    // you'll need to ensure it's mocked or called safely in test environment.
    // The main.dart MyApp already initializes Firebase, but that's for app run, not isolated widget test.
    // One way: Test MyApp, then navigate. Or, provide mock services.

    // For an isolated LoginScreen test, we often mock its dependencies (like AuthService).
    // Given the current setup, we'll test its UI structure.
    await tester.pumpWidget(MaterialApp(home: LoginScreen()));
  }

  testWidgets('LoginScreen UI elements are present', (WidgetTester tester) async {
    await pumpLoginScreen(tester);

    expect(find.widgetWithText(AppBar, 'Parent Login/Register'), findsOneWidget);
    expect(find.widgetWithText(TextFormField, 'Email'), findsOneWidget); // Check by label text if using InputDecoration
    expect(find.widgetWithText(TextFormField, 'Password'), findsOneWidget);
    expect(find.widgetWithText(ElevatedButton, 'Login'), findsOneWidget);
    expect(find.widgetWithText(TextButton, 'Register New Account'), findsOneWidget);
  });

  testWidgets('LoginScreen empty email validation', (WidgetTester tester) async {
    await pumpLoginScreen(tester);
    await tester.tap(find.widgetWithText(ElevatedButton, 'Login'));
    await tester.pump(); // Rebuild the widget after the tap

    expect(find.text('Invalid email'), findsOneWidget); // Assuming this is the error message
    expect(find.text('Password too short'), findsOneWidget); // And for password
  });

   testWidgets('LoginScreen invalid email format validation', (WidgetTester tester) async {
    await pumpLoginScreen(tester);
    await tester.enterText(find.byWidgetPredicate((widget) => widget is TextFormField && widget.decoration?.labelText == 'Email'), 'invalidemail');
    await tester.enterText(find.byWidgetPredicate((widget) => widget is TextFormField && widget.decoration?.labelText == 'Password'), '12345'); // Too short
    await tester.tap(find.widgetWithText(ElevatedButton, 'Login'));
    await tester.pump();

    expect(find.text('Invalid email'), findsOneWidget);
    expect(find.text('Password too short'), findsOneWidget);
  });

  // More tests: successful login navigation (would require mocking AuthService and Navigator)
}
