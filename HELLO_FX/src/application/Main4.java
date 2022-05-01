package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.stage.Stage;


public class Main4 extends Application {
	Button btn;
	TextField tfMine;
	TextField tfCom;
	TextField tfResult;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			Parent root = FXMLLoader.load(getClass().getResource("main4.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			tfMine = (TextField)scene.lookup("#tfMine");
			tfCom = (TextField)scene.lookup("#tfCom");
			tfResult = (TextField)scene.lookup("#tfResult");
			btn = (Button)scene.lookup("#btn");
			btn.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					playGame();
					
				}
				
			});
			
			
			
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void playGame() {
		String result = "";
		String mine = tfMine.getText();
		
		double random = Math.random();
		if(random > 0.5) tfCom.setText("홀");
		else tfCom.setText("짝");
		
		String com = tfCom.getText();
		
		if(mine.equals(com)) result = "이겼습니다.";
		else result = "졌습니다.";
		
		tfResult.setText(result);
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
