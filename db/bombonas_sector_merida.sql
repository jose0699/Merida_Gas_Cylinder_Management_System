-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-06-2024 a las 05:20:18
-- Versión del servidor: 10.4.14-MariaDB
-- Versión de PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bombonas_sector_merida`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `entrega_bombona`
--

CREATE TABLE `entrega_bombona` (
  `id_entraga_bombona` int(11) NOT NULL,
  `fk_usuario` int(11) NOT NULL,
  `fk_tamano` int(11) NOT NULL,
  `fk_estatus_bombona` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `entrega_bombona`
--

INSERT INTO `entrega_bombona` (`id_entraga_bombona`, `fk_usuario`, `fk_tamano`, `fk_estatus_bombona`) VALUES
(1, 3, 2, 1),
(2, 3, 2, 2),
(3, 3, 3, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estatus_bombona`
--

CREATE TABLE `estatus_bombona` (
  `id_estatus` int(11) NOT NULL,
  `descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `estatus_bombona`
--

INSERT INTO `estatus_bombona` (`id_estatus`, `descripcion`) VALUES
(1, 'llenadero'),
(2, 'entregada');
(3, 'no entregada');
(4, 'perdida');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `role`
--

CREATE TABLE `role` (
  `id_role` int(11) NOT NULL,
  `descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `role`
--

INSERT INTO `role` (`id_role`, `descripcion`) VALUES
(1, 'administrador'),
(2, 'cliente');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tamano_bombona`
--

CREATE TABLE `tamano_bombona` (
  `id_bombona` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `tamano_bombona`
--

INSERT INTO `tamano_bombona` (`id_bombona`, `nombre`) VALUES
(1, 'bombona pequeña'),
(2, 'bombona mediana'),
(3, 'bombona grande');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id_usuario` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `cedula` int(20) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `usuario` varchar(100) NOT NULL,
  `contrasena` varchar(100) NOT NULL,
  `fk_role` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id_usuario`, `nombre`, `cedula`, `correo`, `usuario`, `contrasena`, `fk_role`) VALUES
(2, 'administrador', 12345678, 'administrador@gmail.com', 'administrador', 'administrador', 1),
(3, 'jose antonio', 87654321, 'jose@gmail.com', 'jose', 'jose', 2);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `entrega_bombona`
--
ALTER TABLE `entrega_bombona`
  ADD PRIMARY KEY (`id_entraga_bombona`),
  ADD KEY `fk_usuario` (`fk_usuario`),
  ADD KEY `fk_tamano` (`fk_tamano`),
  ADD KEY `fk_estatus_bombona` (`fk_estatus_bombona`);

--
-- Indices de la tabla `estatus_bombona`
--
ALTER TABLE `estatus_bombona`
  ADD KEY `id_estatus` (`id_estatus`);

--
-- Indices de la tabla `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id_role`);

--
-- Indices de la tabla `tamano_bombona`
--
ALTER TABLE `tamano_bombona`
  ADD PRIMARY KEY (`id_bombona`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usuario`),
  ADD KEY `fk_role` (`fk_role`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `entrega_bombona`
--
ALTER TABLE `entrega_bombona`
  MODIFY `id_entraga_bombona` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `estatus_bombona`
--
ALTER TABLE `estatus_bombona`
  MODIFY `id_estatus` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `role`
--
ALTER TABLE `role`
  MODIFY `id_role` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `tamano_bombona`
--
ALTER TABLE `tamano_bombona`
  MODIFY `id_bombona` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `entrega_bombona`
--
ALTER TABLE `entrega_bombona`
  ADD CONSTRAINT `entrega_bombona_ibfk_1` FOREIGN KEY (`fk_usuario`) REFERENCES `usuarios` (`id_usuario`) ON UPDATE CASCADE,
  ADD CONSTRAINT `entrega_bombona_ibfk_2` FOREIGN KEY (`fk_tamano`) REFERENCES `tamano_bombona` (`id_bombona`) ON UPDATE CASCADE,
  ADD CONSTRAINT `entrega_bombona_ibfk_3` FOREIGN KEY (`fk_estatus_bombona`) REFERENCES `estatus_bombona` (`id_estatus`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`fk_role`) REFERENCES `role` (`id_role`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
