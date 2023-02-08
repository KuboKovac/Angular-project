import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {NavComponent} from './nav/nav.component';
import {HomeComponent} from './home/home.component';
import {MatToolbarModule} from "@angular/material/toolbar";
import {MatDialogModule} from "@angular/material/dialog";
import {AddVehicleComponent} from './add-vehicle/add-vehicle.component';
import {LoginComponent} from './login/login.component';
import {RegisterComponent} from './register/register.component';
import {MatInputModule} from "@angular/material/input";
import {MatButtonModule} from "@angular/material/button";
import {HttpClientModule} from "@angular/common/http";
import {MatSnackBarModule} from "@angular/material/snack-bar";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import { VehiclesComponent } from './vehicles/vehicles.component';
import {MatCardModule} from "@angular/material/card";
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import {MatIconModule} from "@angular/material/icon";
import { VehicleDetailComponent } from './vehicle-detail/vehicle-detail.component';
import { FooterComponent } from './footer/footer.component';
import { EditVehicleComponent } from './edit-vehicle/edit-vehicle.component';

@NgModule({
  declarations: [
    AppComponent,
    NavComponent,
    HomeComponent,
    AddVehicleComponent,
    LoginComponent,
    RegisterComponent,
    VehiclesComponent,
    PageNotFoundComponent,
    VehicleDetailComponent,
    FooterComponent,
    EditVehicleComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    ReactiveFormsModule,

    MatToolbarModule,
    MatDialogModule,
    MatButtonModule,
    MatInputModule,
    MatSnackBarModule,
    MatCardModule,
    MatIconModule,

    AppRoutingModule,
    BrowserAnimationsModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
