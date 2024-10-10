package j;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class LibraryApp extends Application {
    @Override
    public void start(Stage primaryStage) throws Exception {
        // Initialize the database
        Database.initialize();

        FXMLLoader loader = new FXMLLoader(getClass().getResource("library.fxml"));
        Scene scene = new Scene(loader.load());
        primaryStage.setScene(scene);
        primaryStage.setTitle("Library Book System");
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
