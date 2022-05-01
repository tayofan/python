package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.stage.Stage;


public class Main7 extends Application {
	
	TextArea ta1;
	TextField tf1;
	TextField tf2;
	Button btn;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			Parent root = FXMLLoader.load(getClass().getResource("main7.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			
			ta1 = (TextArea) scene.lookup("#ta1");
			tf1 = (TextField) scene.lookup("#tf1");
			tf2 = (TextField) scene.lookup("#tf2");
			btn = (Button) scene.lookup("#btn");
			
			btn.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					printStar();
					
				}
			});
			
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void printStar() {
		
		String result = "";
		try {
			int start = Integer.parseInt(tf1.getText());
			int end = Integer.parseInt(tf2.getText());
			
			
			for(int i = start; i < end + 1; i++) {
				for(int j = 1; j < i + 1; j++) {
					result += "*";
				}
				result += "\n";
			}
			
			
		} catch (Exception e) {
			result += "별개수를 입력해주세요";
		}
		ta1.setText(result);
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
