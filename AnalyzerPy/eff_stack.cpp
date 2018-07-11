x//
//  eff_stack.cpp
//  
//
//  Created by Tanvi Wamorkar on 3/21/18.
//
//

void(eff_stack){

TCanvas * c1 = new TCanvas("c1","c1",800,800);
TH1F *h_case1 = new TH1F("h_case1","h_case1",100,0,80);

h_case1->Fill(0.1,0.55);

c1->Draw();


}
