import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {HomeComponent} from "./home/home.component";
import {AddVehicleComponent} from "./add-vehicle/add-vehicle.component";
import {VehiclesComponent} from "./vehicles/vehicles.component";
import {LoginGuard} from "./guards/login.guard";
import {PageNotFoundComponent} from "./page-not-found/page-not-found.component";
import {VehicleDetailComponent} from "./vehicle-detail/vehicle-detail.component";

const routes: Routes = [
  {path: 'home', component: HomeComponent},
  {path: '', component: HomeComponent},
  {path: 'vehicles', component: VehiclesComponent},
  {path: 'addVehicle', component: AddVehicleComponent, canActivate: [LoginGuard]},
  {path: 'vehicles/:id', component: VehicleDetailComponent},
  {path: 'pageNotFound', component: PageNotFoundComponent},
  {path: '**', component: PageNotFoundComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
