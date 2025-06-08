import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:sudo_aprender_brincar/screens/games/escovando_os_dentes/escovando_os_dentes_screen.dart';

void main() {
  testWidgets('EscovandoOsDentesScreen initial state (Step 0)', (WidgetTester tester) async {
    await tester.pumpWidget(const MaterialApp(home: EscovandoOsDentesScreen()));

    expect(find.text('Jogo: Escovando os Dentes (MVP)'), findsOneWidget); // AppBar title
    expect(find.text('Passo 1: Coloque a pasta na escova'), findsOneWidget);
    expect(find.widgetWithText(ElevatedButton, 'Simular aplicar pasta'), findsOneWidget);
  });

  testWidgets('EscovandoOsDentesScreen advances steps on button press', (WidgetTester tester) async {
    await tester.pumpWidget(const MaterialApp(home: EscovandoOsDentesScreen()));

    // Step 0 to 1
    await tester.tap(find.widgetWithText(ElevatedButton, 'Simular aplicar pasta'));
    await tester.pump(); // Process the setState
    expect(find.text('Passo 2: Escove os dentes'), findsOneWidget);

    // Step 1 to 2
    await tester.tap(find.widgetWithText(ElevatedButton, 'Simular escovar'));
    await tester.pump();
    expect(find.text('Passo 3: Enxágue a boca'), findsOneWidget);

    // Step 2 to 3
    await tester.tap(find.widgetWithText(ElevatedButton, 'Simular enxaguar'));
    await tester.pump();
    expect(find.text('Muito bem! Dentes limpinhos!'), findsOneWidget);
    expect(find.widgetWithText(ElevatedButton, 'Voltar ao Lobby'), findsOneWidget);
  });
}
