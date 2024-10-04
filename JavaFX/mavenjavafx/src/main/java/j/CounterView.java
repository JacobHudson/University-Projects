package j;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class CounterView extends Application {
    private Counter model;
    private CounterController controller;

    @Override
    public void start(Stage primaryStage) {
        // Initialize Model and Controller
        model = new Counter();
        controller = new CounterController(model);

        // Create UI controls
        Label countLabel = new Label("Count: 0");
        Button incrementButton = new Button("Increment");

        // Add event handler
        incrementButton.setOnAction(e -> {
            controller.handleIncrement();
            countLabel.setText("Count: " + controller.getCount());
        });

        // Arrange controls in layout
        VBox layout = new VBox(10);
        layout.getChildren().addAll(countLabel, incrementButton);

        // Create scene
        Scene scene = new Scene(layout, 200, 100);

        // Set up stage
        primaryStage.setTitle("MVC Counter");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
