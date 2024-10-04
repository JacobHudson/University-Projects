package j;

import java.io.IOException;
import javafx.fxml.FXML;

public class SecondaryController {

    @FXML
    private void switchToPrimary() throws IOException {
        App.setRoot("primary");
    }

    @FXML
    private void BookNameAction() throws IOException {
        App.setRoot("primary");
    }

    @FXML
    private void AuthorAction() throws IOException{
        App.setRoot("primary");
    }

    @FXML
    private void PublsihedDateAction() throws IOException{
        App.setRoot("primary");
    }

    @FXML
    private void CheckedInAction() throws IOException{
        App.setRoot("primary");
    }
    

    @FXML
    private void AddBookAction() throws IOException{
        
    }
}